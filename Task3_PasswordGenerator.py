import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)
