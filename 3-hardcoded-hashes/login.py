import hashlib

VALID_CREDENTIALS = [
    {
        'username': 'robert',
        'password_hash': 'ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae'
    },
    {
        'username': 'anoosh',
        'password_hash': '3c32608fd9ffd87ae17dbb3a65a509cc8ba5aa395147c99ed20bdba9c434d8c2'
    },
    {
        'username': 'juan',
        'password_hash': '5dc7286295def318e3e643b21ec8963fe1a0d4c43c0e62a7477ad43c4a04406e'
    }
]

def is_valid_credentials(username, password):
    user_stored_creds = None
    for cred in VALID_CREDENTIALS:
        if cred['username'] == username:
            user_stored_creds = cred
            break

    if user_stored_creds is None:
        return False

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return user_stored_creds['password_hash'] == password_hash


if __name__ == "__main__":
    username = input("What is your username?\n")
    password = input("What is your password?\n")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
        print("REVEALING DEEP DARK SECRET...")
        print("I didn't like Stranger Things all that much")

    else:
        print("ACCESS DENIED")
