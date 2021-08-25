from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Key: {key}")

f = Fernet(key)

encrypted_text = f.encrypt(b"python")
print(f"Encrypted text: {encrypted_text}")

decrypted_text = f.decrypt(encrypted_text)
print(f"Decrypted text: {decrypted_text}")
