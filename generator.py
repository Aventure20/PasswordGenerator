import random
character = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn0123456789&#{([-_ç@?./:!§])}"
length = int(input("Which length do you want for your password?\n"))
while True:
    if length < 81:
        break
    else:
        print("Sorry but the max length for your password is =<80")
        print("Please try again:")
        length = int(input("Which length do you want for your password?\n"))
password = "".join(random.sample(character, length))
print(password)
print("Password generated with success")
