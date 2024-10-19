import random
import string

# Create the character set including spaces, punctuation, digits, and letters
chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars)  # Convert to list so we can shuffle
key = chars.copy()   # Copy the list for the key

# Shuffle the key to generate the encryption mapping
random.shuffle(key)

# Print for debugging (optional)
# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPTION
plain_text = input("Enter the message you want to encrypt: ")
cipher_text = ""

# Encrypt each letter by finding its index in 'chars' and using the 'key'
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

# Output the original and encrypted message
print(f"Original message: {plain_text}")   
print(f"Encrypted message: {cipher_text}")  


# DECRYPTION
cipher_text = input("Enter the message you want to decrypt: ")
decrypted_text = ""  # Use a new variable to store decrypted text

# Decrypt each letter by finding its index in 'key' and using the 'chars'
for letter in cipher_text:
    index = key.index(letter)
    decrypted_text += chars[index]

# Output the decrypted message
print(f"Decrypted message: {decrypted_text}")




