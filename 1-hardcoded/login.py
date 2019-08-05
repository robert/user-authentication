VALID_USERNAME = "robert"
VALID_PASSWORD = "test123"

def is_valid_credentials(username, password):
    return username == VALID_USERNAME and password == VALID_PASSWORD

if __name__ == "__main__":
    username = input("What is your username?\n")
    password = input("What is your password?\n")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
        print("REVEALING DEEP DARK SECRET...")
        print("I didn't like Stranger Things all that much")

    else:
        print("ACCESS DENIED")
