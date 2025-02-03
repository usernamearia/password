import random
import string
import pyfiglet
from colorama import Fore, Style, init
import pyperclip 

# Initialize colorama to automatically reset styles after each print
init(autoreset=True)

def generate_password(length=12, use_numbers=True, use_symbols=True):
    # Define character sets for letters, numbers, and symbols
    letters = string.ascii_letters
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    # Combine all selected character sets
    all_chars = letters + numbers + symbols

    # Check if no characters are selected
    if not all_chars:
        print(Fore.RED + "Error: No characters selected for password generation.")
        return None

    # Generate and return a random password
    return ''.join(random.choice(all_chars) for _ in range(length))

def get_user_input(prompt, validation_func=None):
    # Continuously prompt the user until valid input is provided
    while True:
        user_input = input(prompt).strip().lower()
        # Validate input if a validation function is provided
        if validation_func and not validation_func(user_input):
            print(Fore.RED + "Invalid input. Please try again.")
            continue
        return user_input

def validate_length(length):
    # Validate that the input is a positive integer
    try:
        length = int(length)
        return length > 0
    except ValueError:
        return False

def validate_yes_no(response):
    # Validate that the input is either "yes" or "no"
    return response in ["yes", "no"]

def main():
    # Display the program title in a stylized format
    print(Fore.CYAN + pyfiglet.figlet_format("Password Generator"))

    # Prompt the user for the desired password length
    length = int(get_user_input(
        Fore.YELLOW + "🔢 Enter password length: " + Fore.GREEN,
        validate_length
    ))

    # Ask the user if they want to include numbers in the password
    use_numbers = get_user_input(
        Fore.YELLOW + "🔢 Include numbers? (yes/no): " + Fore.GREEN,
        validate_yes_no
    ) == "yes"

    # Ask the user if they want to include symbols in the password
    use_symbols = get_user_input(
        Fore.YELLOW + "🔣 Include symbols? (yes/no): " + Fore.GREEN,
        validate_yes_no
    ) == "yes"

    # Generate the password based on the user's preferences
    password = generate_password(length, use_numbers, use_symbols)
    
    if password:
        # Display the generated password
        print(Fore.MAGENTA + "\n🎉 Generated Password: " + Fore.CYAN + Style.BRIGHT + password)
        print(Fore.LIGHTBLACK_EX + "⚠️ Remember to store your password securely!")

        # Attempt to copy the password to the clipboard
        try:
            pyperclip.copy(password)
            print(Fore.GREEN + "📋 Password copied to clipboard!")
        except Exception as e:
            print(Fore.RED + "❌ Failed to copy password to clipboard. Error: " + str(e))

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()