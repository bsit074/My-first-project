# atbash.py
# Implementation of the Atbash Cipher
# A classical substitution cipher where A ↔ Z, B ↔ Y, C ↔ X, etc.

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                # A (65) -> Z (90), B (66) -> Y (89) ...
                result += chr(90 - (ord(char) - 65))
            else:
                # a (97) -> z (122), b (98) -> y (121) ...
                result += chr(122 - (ord(char) - 97))
        else:
            # Preserve non-alphabet characters
            result += char
    return result


if __name__ == "__main__":
    # Accept plaintext input from the user
    plaintext = input("Enter text to encrypt with Atbash Cipher: ")

    # Encrypt using Atbash Cipher
    encrypted = atbash_cipher(plaintext)
    print("Encrypted text:", encrypted)

    # Decrypt (Atbash is symmetric, so encrypting again decrypts it)
    decrypted = atbash_cipher(encrypted)
    print("Decrypted text:", decrypted)
