import random
character = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn0123456789&#{([-_ç@?./:!§])}"
length = int(input("Combien de caractère doit contenir votre mot de passe?\n"))
while True:
    if length < 81:
        break
    else:
        print("Désolé mais le nombre maximal de caractère que votre mot de passse peut contenir doit être =<80")
        print("Merci de réésayer:")
        length = int(input("Combien de caractère doit contenir votre mot de passe?\n"))
password = "".join(random.sample(character, length))
print(password)
print("Mot de passe généré avec succé!")
