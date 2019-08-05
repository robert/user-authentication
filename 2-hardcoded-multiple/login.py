VALID_CREDENTIALS = [
    {
        'username': 'robert',
        'password': 'test123'
    },
    {
        'username': 'anoosh',
        'password': 'snuffles456'
    },
    {
        'username': 'juan',
        'password': 'happyland'
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

    return user_stored_creds['password'] == password


if __name__ == "__main__":
    username = input("What is your username?\n")
    password = input("What is your password?\n")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
        print("REVEALING DEEP DARK SECRET...")
        print("I didn't like Stranger Things all that much")

    else:
        print("ACCESS DENIED")
