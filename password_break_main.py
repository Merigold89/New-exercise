import random

letters = 'abcdefghijklmnouprstuvwyxyz'
count = 0

while True:
    print("Create password 4 letters only lowercase")
    password = input("Password: ")
    if len(password) == 4:
        if password.lower() == password:
            break
    else:
        print('Password is invalid')
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
        try_password = ""  # wyzeruj try_password
