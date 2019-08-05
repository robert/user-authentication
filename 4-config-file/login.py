import hashlib
import yaml

with open('./credentials.yaml', 'r') as f:
    VALID_CREDENTIALS = yaml.safe_load(f)

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
