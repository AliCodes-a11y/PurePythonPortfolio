# main.py

# --- رنگ‌ها ---
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

# مسیر فایل کاربران
USER_FILE = "users.txt"

# --- تابع خوشامدگویی با ASCII Art ---
def welcome():
    print(CYAN + """
 __  __       _ _   _       __  __                                    
|  \/  | __ _(_) |_| |__   |  \/  | ___  ___ ___  __ _  __ _  ___ _ __ 
| |\/| |/ _` | | __| '_ \  | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \ '__|
| |  | | (_| | | |_| | | | | |  | |  __/\__ \__ \ (_| | (_| |  __/ |   
|_|  |_|\__,_|_|\__|_| |_| |_|  |_|\___||___/___/\__,_|\__, |\___|_|   
                                                       |___/           
""" + RESET)

# --- بررسی قدرت پسورد ---
def is_strong_password(password):
    if len(password) < 6:
        print(RED + "Password too short! Must be at least 6 characters." + RESET)
        return False
    if not any(c.isupper() for c in password):
        print(RED + "Password must contain at least one uppercase letter." + RESET)
        return False
    if not any(c.isdigit() for c in password):
        print(RED + "Password must contain at least one number." + RESET)
        return False
    return True

# --- ثبت‌نام ---
def sign_up():
    username = input(CYAN + "Enter new username: " + RESET)
    password = input(CYAN + "Enter new password: " + RESET)

    if not is_strong_password(password):
        return

    # بررسی نام کاربری تکراری
    try:
        with open(USER_FILE, "r") as file:
            users = file.readlines()
            for user in users:
                u, _ = user.strip().split(":")
                if u == username:
                    print(RED + "Username already exists!" + RESET)
                    return
    except FileNotFoundError:
        pass  # اگر فایل موجود نبود، ادامه بده

    with open(USER_FILE, "a") as file:
        file.write(f"{username}:{password}\n")
    print(GREEN + "User registered successfully!" + RESET)

# --- لاگین ---
def login():
    username = input(CYAN + "Username: " + RESET)
    attempts = 0
    while attempts < 3:
        password = input(CYAN + "Password: " + RESET)
        try:
            with open(USER_FILE, "r") as file:
                users = file.readlines()
                for user in users:
                    u, p = user.strip().split(":")
                    if u == username and p == password:
                        print(GREEN + "Login successful!" + RESET)
                        return True
        except FileNotFoundError:
            print(YELLOW + "No users registered yet!" + RESET)
            return False
        attempts += 1
        print(RED + f"Incorrect credentials. Attempts left: {3 - attempts}" + RESET)
    print(RED + "Too many failed attempts! Try again later." + RESET)
    return False

# --- لاگین بدون محدودیت برای تغییر رمز و حذف ---
def login_user(username):
    try:
        with open(USER_FILE, "r") as file:
            users = file.readlines()
            password = input(CYAN + "Password: " + RESET)
            for user in users:
                u, p = user.strip().split(":")
                if u == username and p == password:
                    return True
    except FileNotFoundError:
        print(YELLOW + "No users registered yet!" + RESET)
        return False
    print(RED + "Incorrect credentials!" + RESET)
    return False

# --- تغییر رمز عبور ---
def change_password():
    username = input(CYAN + "Enter your username: " + RESET)
    if not login_user(username):
        return
    new_password = input(CYAN + "Enter new password: " + RESET)
    if not is_strong_password(new_password):
        return
    with open(USER_FILE, "r") as file:
        users = file.readlines()
    with open(USER_FILE, "w") as file:
        for user in users:
            u, p = user.strip().split(":")
            if u == username:
                file.write(f"{u}:{new_password}\n")
            else:
                file.write(f"{u}:{p}\n")
    print(GREEN + "Password changed successfully!" + RESET)

# --- حذف کاربر ---
def delete_user():
    username = input(CYAN + "Enter username to delete: " + RESET)
    if not login_user(username):
        return
    with open(USER_FILE, "r") as file:
        users = file.readlines()
    with open(USER_FILE, "w") as file:
        found = False
        for user in users:
            u, p = user.strip().split(":")
            if u != username:
                file.write(f"{u}:{p}\n")
            else:
                found = True
    if found:
        print(GREEN + f"User '{username}' deleted successfully!" + RESET)
    else:
        print(RED + "User not found." + RESET)

# --- منوی اصلی ---
def main():
    welcome()
    while True:
        print(YELLOW + "\n--- User Management System ---" + RESET)
        print(BLUE + "1. Sign Up" + RESET)
        print(BLUE + "2. Login" + RESET)
        print(BLUE + "3. Change Password" + RESET)
        print(BLUE + "4. Delete User" + RESET)
        print(BLUE + "5. Exit" + RESET)
        choice = input(CYAN + "Choose an option: " + RESET)

        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            change_password()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print(GREEN + "Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid option." + RESET)

if __name__ == "__main__":
    main()
