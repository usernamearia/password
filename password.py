import random
import string
import pyfiglet
from colorama import Fore, Style, init
import pyperclip  # Library for clipboard operations

# Initialize colorama for Windows compatibility
init(autoreset=True)

def generate_password(length=12, use_numbers=True, use_symbols=True):
    """Generates a random password with customizable options."""
    letters = string.ascii_letters
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = letters + numbers + symbols

    if not all_chars:
        print(Fore.RED + "Error: No characters selected for password generation.")
        return None

    return ''.join(random.choice(all_chars) for _ in range(length))

def get_user_input(prompt, validation_func=None):
    """Helper function to get user input with optional validation."""
    while True:
        user_input = input(prompt).strip().lower()
        if validation_func and not validation_func(user_input):
            print(Fore.RED + "Invalid input. Please try again.")
            continue
        return user_input

def validate_length(length):
    """Validate that the password length is a positive integer."""
    try:
        length = int(length)
        return length > 0
    except ValueError:
        return False

def validate_yes_no(response):
    """Validate that the response is either 'yes' or 'no'."""
    return response in ["yes", "no"]

def main():
    """Runs the interactive password generator."""
    print(Fore.CYAN + pyfiglet.figlet_format("Password Generator"))

    # Get password length with validation
    length = int(get_user_input(
        Fore.YELLOW + "🔢 Enter password length: " + Fore.GREEN,
        validate_length
    ))

    # Get whether to include numbers with validation
    use_numbers = get_user_input(
        Fore.YELLOW + "🔢 Include numbers? (yes/no): " + Fore.GREEN,
        validate_yes_no
    ) == "yes"

    # Get whether to include symbols with validation
    use_symbols = get_user_input(
        Fore.YELLOW + "🔣 Include symbols? (yes/no): " + Fore.GREEN,
        validate_yes_no
    ) == "yes"

    # Generate the password
    password = generate_password(length, use_numbers, use_symbols)
    
    if password:
        # Display the password
        print(Fore.MAGENTA + "\n🎉 Generated Password: " + Fore.CYAN + Style.BRIGHT + password)
        print(Fore.LIGHTBLACK_EX + "⚠️ Remember to store your password securely!")

        # Copy the password to the clipboard
        try:
            pyperclip.copy(password)
            print(Fore.GREEN + "📋 Password copied to clipboard!")
        except Exception as e:
            print(Fore.RED + "❌ Failed to copy password to clipboard. Error: " + str(e))

if __name__ == "__main__":
    main()