import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# global variable

totalc = 0


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    loop = db.execute("SELECT * FROM current WHERE user_id = ?", session["user_id"])


    newprice = 0
    for i in range(len(loop)):
        newprice = lookup(loop[i]["stock"])
        db.execute("UPDATE current SET price = ?, total = ?, time = ? WHERE user_id = ? AND stock = ?", newprice["price"], newprice["price"] * loop[i]["shares"], newprice["time"], session["user_id"], loop[i]["stock"])

    summ = 0
    stock = db.execute("SELECT * FROM current WHERE user_id = ? ORDER BY stock", session["user_id"])
    for i in range(len(stock)):
        summ = summ + stock[i]["total"]
    totalc = cash[0]["cash"] + summ

    return render_template("index.html", stock=stock, len=len(stock), cash=cash[0]["cash"], totalc=int(totalc))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Please enter the Symbol", 400)
        elif not shares or not str.isnumeric(shares) or int(shares) <= 0:
            return apology("Please enter valid shares", 400)

        # get price from chosen symbol
        price = lookup(symbol)
        if price == None:
            return apology("Please type valid stock", 400)

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # check for enough money on account
        if cash[0]["cash"] < price["price"] * int(shares):
            return apology("You dont have enough money to purchase", 405)

        Bought = 'Bought'

        db.execute("INSERT INTO purchase (user_id, price, shares, stocks, trans) VALUES(?, ?, ?, ?, ?)",session["user_id"], price["price"] * int(shares), shares, symbol, Bought)
        # Update cash from user
        update = cash[0]["cash"] - (price["price"] * int(shares))
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update, session["user_id"])

        curr = db.execute("SELECT total, shares FROM current WHERE stock = ? AND user_id = ?", symbol, session["user_id"])

        if len(curr) == 0:
            db.execute("INSERT OR IGNORE INTO current (stock, price, shares, user_id, name, total, time) VALUES(?, ?, ?, ?, ?, ?, ?)", symbol , price["price"], shares, session["user_id"], price["name"], int(price["price"]) * int(shares), price["time"])
        else:
            db.execute("UPDATE current SET total = ?, shares = ? WHERE stock = ? AND user_id = ?", (int(price["price"]) * int(shares)) + int(curr[0]["total"]), int(shares) + int(curr[0]["shares"]), symbol, session["user_id"])

        return redirect("/")

    return render_template("buy.html")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stock = db.execute("SELECT price, shares, timestamp, stocks, trans FROM purchase WHERE user_id = ? ORDER BY timestamp DESC", session["user_id"])
    leng = len(stock)
    return render_template("history.html" ,stock=stock, len=leng)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please type a symbol", 400)
        stock = lookup(symbol)
        if stock == None:
            return apology("Please type valid stock", 400)
        return render_template("quoted.html", stock=stock, symbol=symbol)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        ur = request.form.get("username")
        pr = request.form.get("password")
        prc = request.form.get("confirmation")
        usercheck = db.execute("SELECT * FROM users")

        # check for userinput
        if not ur:
            return apology("must provide username", 400)
        elif not pr:
            return apology("must provide password", 400)
        elif not prc:
            return apology("need to confirm password", 400)

        # check if list is empty
        if len(usercheck) == 0:
            if pr == prc:
                pr = generate_password_hash(pr)
                db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",ur, pr)
                return redirect("/login")
            else:
                return apology("Passwords are not the same", 400)

        else:
        # check if username exist

            for i in range(len(usercheck)):

                if ur in usercheck[i]["username"]:
                    # check if password and confirm password is equal, if so generate hash
                    return apology("User already exist", 400)

        if pr == prc:
            pr = generate_password_hash(pr)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",ur, pr)
            return redirect("/login")
        else:
            return apology("Passwords are not the same", 400)

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Please enter the Symbol", 400)
        elif not shares:
            return apology("Please enter the amount of shares", 400)

        # get price from chosen symbol
        price = lookup(symbol)
        if price == None:
            return apology("Please type valid stock", 400)
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # check for enough shares from stock
        curr = db.execute("SELECT * FROM current WHERE stock = ? AND user_id = ?", symbol, session["user_id"])
        if len(curr) == 0:
            return apology("You dont have any shares so far", 400)
        elif int(shares) > curr[0]["shares"]:
            return apology("You dont have enough shares from this stock to Sell", 400)

        Sold = 'Sold'
        db.execute("INSERT INTO purchase (user_id, price, shares, stocks, trans) VALUES(?, ?, ?, ?, ?)",session["user_id"], price["price"] * int(shares), shares, symbol, Sold)
        # Update cash from user
        update = cash[0]["cash"] + (price["price"] * int(shares))
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update, session["user_id"])

        db.execute("UPDATE current SET total = ?, shares = ? WHERE stock = ? AND user_id = ?", int(curr[0]["total"]) - (int(price["price"]) * int(shares)), int(curr[0]["shares"] - int(shares)), symbol, session["user_id"])

        db.execute("DELETE FROM current WHERE shares = 0 AND user_id = ?", session["user_id"])

        return redirect("/")

    value = db.execute("SELECT stock FROM current WHERE user_id = ?", session["user_id"])

    return render_template("sell.html", value=value, len=len(value))


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():

    if request.method == "POST":
        user = request.form.get("username")
        p1 = request.form.get("password1")
        p2 = request.form.get("password2")

        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if p1 != p2:
            return apology("Passwords are not the same", 400)
        elif not check_password_hash(rows[0]["hash"], p1) or rows[0]["username"] != user:
            return apology("Invalid Username or Password",  400)

        db.execute("DELETE FROM users WHERE id = ?", session["user_id"])

        return redirect("/logout")


    return render_template("/delete.html")