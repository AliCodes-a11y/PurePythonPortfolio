# encryption_tool.py

# رنگ‌ها
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

# --- Caesar Cipher ---
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- XOR Cipher ---
def xor_encrypt_decrypt(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

# --- منوی اصلی ---
def main():
    print(CYAN + "\n--- Simple Encryption Tool ---" + RESET)
    while True:
        print(YELLOW + "\nChoose method:" + RESET)
        print(BLUE + "1. Caesar Cipher" + RESET)
        print(BLUE + "2. XOR Cipher" + RESET)
        print(BLUE + "3. Exit" + RESET)
        choice = input(CYAN + "Your choice: " + RESET)

        if choice == "1":
            text = input(CYAN + "Enter text: " + RESET)
            shift = int(input(CYAN + "Enter shift number: " + RESET))
            action = input(CYAN + "Encrypt or Decrypt? (E/D): " + RESET).upper()
            if action == "E":
                print(GREEN + "Encrypted text: " + caesar_encrypt(text, shift) + RESET)
            elif action == "D":
                print(GREEN + "Decrypted text: " + caesar_decrypt(text, shift) + RESET)
            else:
                print(RED + "Invalid option!" + RESET)

        elif choice == "2":
            text = input(CYAN + "Enter text: " + RESET)
            key = int(input(CYAN + "Enter numeric key: " + RESET))
            action = input(CYAN + "Encrypt or Decrypt? (E/D): " + RESET).upper()
            if action in ["E", "D"]:
                print(GREEN + "Result: " + xor_encrypt_decrypt(text, key) + RESET)
            else:
                print(RED + "Invalid option!" + RESET)

        elif choice == "3":
            print(GREEN + "Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid choice!" + RESET)

if __name__ == "__main__":
    main()
