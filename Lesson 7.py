import sqlite3
import hashlib

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ======= CREATE ========
# cur.execute("CREATE TABLE users (login TEXT, password TEXT, email TEXT);")
# connection.commit()


# ======= INSERT ========
login = input("Login    : ")
passw = input("Password : ")
email = input("Email    : ")
h = hashlib.sha256()
h.update(b"{passw}")
h_pass = h.hexdigest()
cur.execute(f"INSERT INTO users (login, password, email) VALUES ('{login}', '{h_pass}', '{email}')")
connection.commit()




connection.close()