# Atbash Cipher 🔐

This project implements the **Atbash Cipher**, a classical substitution cipher that simply reverses the alphabet.

- A ↔ Z  
- B ↔ Y  
- C ↔ X  
- ...  
- a ↔ z  
- b ↔ y  
- c ↔ x  

### Features
- Handles both **uppercase** and **lowercase** letters.
- Keeps **non-alphabetic characters** (spaces, punctuation) unchanged.
- Works the same for **encryption** and **decryption** since Atbash is symmetric.

### How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/atbash_cipher.git
   cd atbash_cipher
   python atbash.py
   Enter text to encrypt with Atbash Cipher: Hello, World!
Encrypted text: Svool, Dliow!
Decrypted text: Hello, World!
