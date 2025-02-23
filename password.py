import random
import string
import pyfiglet
from colorama import Fore, Style, init
import pyperclip 

# Initialize colorama to automatically reset styles after each print
init(autoreset=True)

# Minimum password length
MIN_PASSWORD_LENGTH = 8

def generate_password(length=16, use_numbers=True, use_symbols=True):
    # Ensure the password is at least the minimum length
    length = max(length, MIN_PASSWORD_LENGTH)

    # Define character sets
    letters = string.ascii_letters
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    # Check if at least one character set is selected
    if not any([letters, numbers, symbols]):
        print(Fore.RED + "Error: No characters selected for password generation.")
        return None

    # Ensure at least one number and one symbol if required
    required_chars = []
    if use_numbers:
        required_chars.append(random.choice(numbers))
    if use_symbols:
        required_chars.append(random.choice(symbols))

    # Fill the rest of the password length with a mix of characters
    all_chars = letters + numbers + symbols
    remaining_chars = [random.choice(all_chars) for _ in range(length - len(required_chars))]

    # Combine required characters with the rest and shuffle for randomness
    password_chars = required_chars + remaining_chars
    random.shuffle(password_chars)

    return ''.join(password_chars)

def get_user_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt).strip().lower()
        if validation_func and not validation_func(user_input):
            print(Fore.RED + "Invalid input. Please try again.")
            continue
        return user_input

def validate_length(length):
    try:
        length = int(length)
        return length >= MIN_PASSWORD_LENGTH  # Ensure minimum security length
    except ValueError:
        return False

def validate_yes_no(response):
    return response in ["yes", "no"]

def main():
    print(Fore.CYAN + pyfiglet.figlet_format("Password Generator"))

    length = int(get_user_input(
        Fore.YELLOW + f"🔢 Enter password length (min {MIN_PASSWORD_LENGTH}): " + Fore.GREEN,
        validate_length
    ))

    use_numbers = get_user_input(
        Fore.YELLOW + "🔢 Include numbers? (yes/no): " + Fore.GREEN,
        validate_yes_no
    ) == "yes"

    use_symbols = get_user_input(
        Fore.YELLOW + "🔣 Include symbols? (yes/no): " + Fore.GREEN,
        validate_yes_no
    ) == "yes"

    password = generate_password(length, use_numbers, use_symbols)

    if password:
        print(Fore.MAGENTA + "\n🎉 Generated Password: " + Fore.CYAN + Style.BRIGHT + password)
        print(Fore.LIGHTBLACK_EX + "⚠️ Remember to store your password securely!")

        try:
            pyperclip.copy(password)
            print(Fore.GREEN + "📋 Password copied to clipboard!")
        except Exception as e:
            print(Fore.RED + "❌ Failed to copy password to clipboard. Error: " + str(e))

if __name__ == "__main__":
    main()
