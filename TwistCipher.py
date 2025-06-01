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

# Example
message = "HelloWorld!"
secret_key = "MyKey"
cipher = encrypt_twistcipher(message, secret_key)
print("Encrypted:", cipher)
original = decrypt_twistcipher(cipher, secret_key)
print("Decrypted:", original)