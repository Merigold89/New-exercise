import random

letters = 'abcdefghijklmnouprstuvwyxyz'
count = 0

print("Create password 4 letters only lowercase")
password = input("Password: ")

if len(password) == 4:
    pass
else:
    print('Password is invalid')
    exit(0)

try_password = ''

while True:
    for i in range(4):
        letter = random.choice(letters)
        try_password += letter
        count += 1
    if try_password == password:
        print("Your password was crakced:", try_password)
        print(f"Sprawdzono {count} kombinacji.")
        break
    else:
        try_password = ""  # wyzeru try_password