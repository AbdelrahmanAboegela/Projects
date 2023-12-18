import random
import string

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

length = int(input("Enter password length: "))
password = generate_password(length)
print("Your password is:", password)
