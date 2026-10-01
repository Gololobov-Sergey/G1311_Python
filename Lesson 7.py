import sqlite3
import hashlib

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ======= CREATE ========
# cur.execute("CREATE TABLE users (login TEXT, password TEXT, email TEXT);")
# connection.commit()


# ======= INSERT ========
# login = input("Login    : ")
# passw = input("Password : ")
# email = input("Email    : ")
# h = hashlib.sha256()
# h.update(passw.encode('utf-8'))
# h_pass = h.hexdigest()
# cur.execute(f"INSERT INTO users (login, password, email) VALUES ('{login}', '{h_pass}', '{email}')")
# connection.commit()

# ====== SELECT =========
# # cur.execute(f"SELECT * FROM users")
# cur.execute(f"SELECT * FROM users WHERE login = 'serg'")
# connection.commit()
# res = cur.fetchall()
# for el in res:
#     print(el)


# ====== UPDATE ========
# cur.execute(f"UPDATE users SET login = 'serg' WHERE rowid = 1")
# connection.commit()


# ===== DELETE ========
cur.execute(f"DELETE FROM users WHERE rowid = 1")
connection.commit()


connection.close()