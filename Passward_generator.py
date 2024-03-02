import string
import secrets

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Please enter a valid integer.")

while True:
    print('''Choose one Option for your password generation:
             1. Letters
             2. Digits
             3. Special Characters
             4. Exit''')

    choice = int(input("Pick a choice for password generation:  "))

    if choice == 4:
        print("Exiting Program")
        break

    if choice in [1, 2, 3]:
        character_set = ""
        if choice == 1:
            character_set = string.ascii_letters
        elif choice == 2:
            character_set = string.digits
        elif choice == 3:
            character_set = string.punctuation

        password = ''.join(secrets.choice(character_set) for _ in range(length))
        print("Your password is " + password)
    else:
        print("Please pick a valid option!")
