 # test table später löschen
    loops = db.execute("SELECT SUM(shares), price, user_id, stocks FROM purchase WHERE user_id = ? AND trans = 'Bought' GROUP BY stocks ORDER BY stocks", session["user_id"])

    stocks= []
    summs = 0
    for i in range(len(loops)):
        price = lookup(loops[i]["stocks"])
        stocks.append({"price": price["price"], "shares": loops[i]["SUM(shares)"], "total": price["price"] * loops[i]["SUM(shares)"], "stock": loops[i]["stocks"]})
        summs = summs + stocks[i]["total"]
    totalt = cash[0]["cash"] + summs

    # letzen drei löschen später
    return render_template("index.html", stock=stock, len=len(stock), cash=cash[0]["cash"], totalc=int(totalc), stocks=stocks, lent=len(stocks), totalt=totalt)


    <!--test table später löschen!-->

    <table>
        <thead>
            <tr>
                <th>Stock</th>
                <th>Shares</th>
                <th>Price</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            {% for i in range(lent) %}
            <tr>
                <td>{{ stocks[i]["stock"] }}</td>
                <td>{{ stocks[i]["shares"] }}</td>
                <td>{{ stocks[i]["price"] | usd }}</td>
                <td>{{ stocks[i]["total"] | usd }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    <table>
        <thead>
            <tr>
                <th>Total Money</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Cash: {{ cash | usd}}</td>
            </tr>
            <tr>
                <td>Total: {{ totalt | usd}}</td>
            </tr>
        </tbody>
    </table>
