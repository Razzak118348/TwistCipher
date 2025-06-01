# TwistCipher - A Novel Symmetric Encryption Algorithm

## Submitted By: Abdur Razzak
## Subject: Mathematical Analysis for Computer Science
## Instructor's Name :Pankaj Bhowmik(Lecturer)

## 🔒 Overview
**TwistCipher** is a simple, symmetric key encryption algorithm developed for educational purposes. It combines character position, ASCII values, and a user-defined key to perform encryption and decryption. This cipher helps beginners understand how encryption logic works.

---

## 📘 Features
- Symmetric key encryption (same key used for encryption and decryption)
- ASCII-based character transformation
- Position-aware ciphering logic
- Simple and readable Python implementation

---

## 🧠 Concept & Working Principle
For each character:
- Take ASCII value of plaintext character
- Add ASCII value of corresponding key character
- Add position index `i`
- Take modulo 256 to ensure it fits within byte range

### 🔐 Encryption Formula
```python
new_char = (ord(plaintext[i]) + ord(key[i]) + i) % 256
```

### 🔓 Decryption Formula
```python
original_char = (ord(ciphertext[i]) - ord(key[i]) - i) % 256
```

---

## 💻 Python Implementation
```python
def encrypt_twistcipher(plaintext, key):
    cipher = []
    key_sequence = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]

    for i in range(len(plaintext)):
        encrypted_char = (ord(plaintext[i]) + ord(key_sequence[i]) + i) % 256
        cipher.append(chr(encrypted_char))

    return ''.join(cipher)

def decrypt_twistcipher(ciphertext, key):
    plaintext = []
    key_sequence = (key * ((len(ciphertext) // len(key)) + 1))[:len(ciphertext)]

    for i in range(len(ciphertext)):
        decrypted_char = (ord(ciphertext[i]) - ord(key_sequence[i]) - i) % 256
        plaintext.append(chr(decrypted_char))

    return ''.join(plaintext)

# Example Usage
message = "HelloWorld!"
secret_key = "MyKey"
cipher = encrypt_twistcipher(message, secret_key)
print("Encrypted:", cipher)
original = decrypt_twistcipher(cipher, secret_key)
print("Decrypted:", original)
```

---

## 📦 Sample Output
```
Encrypted: ÕëõûÙõÿöÜ
Decrypted: HelloWorld!
```

---

## 🔐 Security Notes
> **Disclaimer:** TwistCipher is not secure for real-world applications. It is designed purely for educational use to demonstrate the concept of symmetric encryption.

---

## 🚀 Future Improvements
- Support for binary and hexadecimal formats
- Use of random nonce or salt to enhance security
- Statistical analysis for cryptanalysis resistance

---

## 📚 License
This project is free to use for educational and academic purposes.
