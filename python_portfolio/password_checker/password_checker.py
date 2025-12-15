# password_checker.py

# رنگ‌ها
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"

# بررسی قدرت پسورد
def check_password(password):
    score = 0
    length = len(password)

    if length >= 6:
        score += 1
    else:
        print(RED + "Password too short (min 6 characters)." + RESET)
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        print(YELLOW + "Add at least one uppercase letter." + RESET)

    if any(c.islower() for c in password):
        score += 1
    else:
        print(YELLOW + "Add at least one lowercase letter." + RESET)

    if any(c.isdigit() for c in password):
        score += 1
    else:
        print(YELLOW + "Add at least one number." + RESET)

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        print(YELLOW + "Add at least one special character (!@#$...)." + RESET)

    # نمایش امتیاز
    if score <= 2:
        print(RED + f"Password strength: Weak ({score}/5)" + RESET)
    elif score == 3 or score == 4:
        print(YELLOW + f"Password strength: Medium ({score}/5)" + RESET)
    else:
        print(GREEN + f"Password strength: Strong ({score}/5)" + RESET)

# منوی ساده
def main():
    print(CYAN + "\n--- Password Strength Checker ---" + RESET)
    while True:
        password = input(CYAN + "Enter password to check (or 'exit' to quit): " + RESET)
        if password.lower() == "exit":
            print(GREEN + "Goodbye!" + RESET)
            break
        check_password(password)

if __name__ == "__main__":
    main()
