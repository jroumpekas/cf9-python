import string
import random

characters = list(string.ascii_letters + string.digits + "!@%#^&")

def generate_password():
    """
    Generate a random password based on the user-specified length.
    """

    try:
        password_length = int(input("Please give the password length: "))

        if password_length <= 0:
            print("Password length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer. ")
        return
    
    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)
        print(f"\nGenerated password: {password}")

def main():
    while True:
        option = input("Do you wnt to create a password? ('y' or 'q' for quit)")

        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'q':
            print("Goodbye")
            break
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()