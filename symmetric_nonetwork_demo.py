from cryptography import fernet


key = fernet.Fernet.generate_key()
print(key)
cipher = fernet.Fernet(key)


## SYMMETRIC ENCRYPTION / DECRYPTION DEMO
message = "This is a secret message"
print(message)
encoded_message = message.encode()
print(encoded_message)
encrypted_message = cipher.encrypt(encoded_message)
print(encrypted_message)
decrypted_message = cipher.decrypt(encrypted_message)
print(decrypted_message)
decoded_message = decrypted_message.decode()
print(decoded_message)