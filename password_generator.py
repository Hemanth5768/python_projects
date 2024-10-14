import random
import string

def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_special_chars)
        print("Generated password:", password)
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
