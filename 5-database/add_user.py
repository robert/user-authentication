import hashlib
import sqlite3

DB_NAME = "ppab6.db"

def is_username_available(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    res = c.execute("""
        SELECT *
        FROM users
        WHERE
          username = ?
    """, (username,)).fetchone()

    return res is None


def add_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    c.execute("""
        INSERT INTO
            users (username, password_hash)
        VALUES
            (?, ?)
    """, (username, password_hash))
    conn.commit()


if __name__ == "__main__":
    print("Let's create your user account!")

    while True:
        username = input("What is your username?\n")
        if is_username_available(username):
            print("Username is available!")
            break
        else:
            print("Username is taken. Choose another one.")

    password = input("What is your password?\n")

    add_user(username, password)
    print("Added %s to the database!" % username)
