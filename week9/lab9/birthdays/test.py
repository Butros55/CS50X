from cs50 import SQL

db = SQL("sqlite:///birthdays.db")

test = db.execute("SELECT name FROM birthdays")

for key in test:
    print(key)

if 'a' in test:
    print('worked')