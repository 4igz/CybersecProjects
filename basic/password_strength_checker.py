import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"

    strength_criteria = [
        re.search("[a-z]", password),
        re.search("[A-Z]", password),
        re.search("[0-9]", password),
        re.search("[!@#$%^&*(),.?\":{}|<>]", password)
    ]

    if all(strength_criteria):
        return "Strong"
    elif any(strength_criteria):
        # In other words if it meets more than one criteria then it's medium, otherwise it's weak
        if sum(bool(criteria) for criteria in strength_criteria) > 1:
            return "Medium"
        else:
            return "Weak"

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(check_password_strength(password))