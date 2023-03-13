#random password generator
import random
import string

chars = list(string.ascii_letters+string.digits+'#@$%&^*)(_+')
random.shuffle(chars)
password = []
i=0
while i < 10:
    password.append(random.choice(chars))
    i += 1
random.shuffle(password)
print("".join(password))