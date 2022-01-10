import secrets

MAXIMUM_PASSWORD_LENGTH = 80

characters = r"AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn0123456789&#{([-_@?./\"':!])}"
password_length = int(input("How long would you like your password?: "))
while True:
    if password_length <= MAXIMUM_PASSWORD_LENGTH:
        break
    else:
        print(f"Password must be below {MAXIMUM_PASSWORD_LENGTH} characters in length.")
        print("Please try again: ")
        password_length = int(input("How long would you like your password?: "))
password = "".join(secrets.choice(characters) for i in range(0, password_length + 1))
print(password)
print("Password successfully generated.")
