import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, digit, and special character
    if (not re.search(r'[A-Z]', password) or
        not re.search(r'[a-z]', password) or
        not re.search(r'\d', password) or
        not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return False

    return True

# Take user input
password = input("Enter a password to check its strength: ")

if check_password_strength(password):
    print("Strong password ✅")
else:
    print("Weak password ❌. Password must be at least 8 characters long, "
          "contain uppercase and lowercase letters, a digit, and a special character.")
