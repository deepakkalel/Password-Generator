# Detailed Password Generator in Python

This project contains a Python script (`passwordgenerator.py`) for generating secure random passwords.

## How it Works
The script generates passwords by ensuring a mix of character types to enhance security. Each generated password includes:
- At least one digit (0-9).
- At least one uppercase letter (A-Z).
- At least one lowercase letter (a-z).
- At least one symbol from a predefined set (e.g., !@#$%^&*).

The generated passwords have a fixed maximum length of 12 characters.

## Code Logic
The script follows these steps to generate a password:
1. **Minimum Requirements Fulfillment:** It starts by picking one random character from each of the required sets: digits, uppercase letters, lowercase letters, and symbols. This ensures the password meets the basic complexity criteria.
2. **Filling Remaining Length:** After the initial four characters are selected, the script fills the rest of the password (up to the maximum length of 12) by randomly selecting characters from a combined list that includes all digits, uppercase letters, lowercase letters, and symbols.
3. **Shuffling for Randomness:** To ensure the characters are not in a predictable order (e.g., digit, uppercase, lowercase, symbol, followed by random characters), the script converts the temporary password string into a list of characters (e.g., using `list(temp_pass)` or similar, conceptually what `array.array('u', temp_pass)` might be used for before conversion to a list). This list is then shuffled using `random.shuffle(temp_pass_list)` to randomize the positions of all characters.
4. **Final Password:** The shuffled list of characters is then joined back into a string to form the final password.

The use of `array.array('u', temp_pass)` (though typically a direct conversion to a list like `list(temp_pass)` is more common for strings before shuffling) and `random.shuffle()` are key to ensuring that the resulting password is not easily guessable based on character placement patterns.

## Usage
To run the script, navigate to the directory containing `passwordgenerator.py` and execute the following command in your terminal:
```bash
python passwordgenerator.py
```
The script will then generate a random password and print it to the console.

ref: https://www.geeksforgeeks.org/generating-strong-password-using-python/
