import hashlib
import sqlite3

DB_NAME = "ppab6.db"

def is_valid_credentials(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    res = c.execute("""
        SELECT *
        FROM users
        WHERE
          username = ? AND
          password_hash = ?
    """, (username, password_hash)).fetchone()

    return res is not None


if __name__ == "__main__":
    username = input("What is your username?\n")
    password = input("What is your password?\n")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
        print("REVEALING DEEP DARK SECRET...")
        print("I didn't like Stranger Things all that much")

    else:
        print("ACCESS DENIED")
