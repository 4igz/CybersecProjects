import random
import string

def generatePassword(len: int) -> str:
    # Generate a password of the given length from all given characters (letters, digits, punctuation)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=len))
    return password

if __name__ == "__main__":
    password_length = None
    while not password_length:
        try:
            password_length = int(input("Enter the length of the password: "))
        except ValueError:
            print("Please enter a valid number.")

    print(generatePassword(int(password_length)))