import string
import argparse

# Defining the alphabet and a space
alphabet = string.ascii_lowercase + " "
letters = {i: char for i, char in enumerate(alphabet)}  # Mapping index to letter
letters_rev = {char: i for i, char in enumerate(alphabet)}  # Reverse mapping for decoding

# Setting up argparse for input handling
p = argparse.ArgumentParser(description="Implement Caesar Cipher Algorithm")
p.add_argument("-e", "--encryption_key", type=int, help="Encryption key", required=True)
p.add_argument("-m", "--message", help="Message to encrypt or decrypt", required=True)
args = p.parse_args()

# Ensuring encryption_key is not None and is an integer
if args.encryption_key is None:
    raise ValueError("Encryption key is required and must be an integer.")
if not isinstance(args.encryption_key, int):
    raise TypeError("Encryption key must be an integer.")

# Message to encode/decode
message = args.message  # Correctly access message argument
encryption_key = args.encryption_key  # Correctly access encryption_key

# Debugging: printing out values of message and encryption_key
print(f"Message: {message}")
print(f"Encryption key: {encryption_key}")

def caesar(mee, encryption_key):
    encrypted_message = ""
    alphabet_length = len(alphabet)

    # For each character in the message, apply the Caesar cipher
    for char in mee:
        if char != " ":
            # Get the current index of the character in the alphabet
            index = letters_rev[char]
            # Apply the encryption key shift 
            new_index = (index + encryption_key) % alphabet_length
            encrypted_message += letters[new_index]
        else:
            # Keeping spaces intact
            encrypted_message += " "

    return encrypted_message

# Encrypt the message
encoded_message = caesar(message, encryption_key)
print(f"Encoded message: {encoded_message}")

# Decrypt using negative key
decoded_message = caesar(encoded_message, -encryption_key)
print(f"Decoded message: {decoded_message}")
