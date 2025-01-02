import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters."
    if not re.search("[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return "Weak: Password must contain at least one digit."
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Moderate: Add a special character for better security."
    return "Strong: Your password is secure."

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print(check_password_strength(user_password))
