from cryptography.fernet import Fernet

# Class to prevent accidental print/log of password
class FakeStr(str):
    def __str__(self):
        return "****"

    def __repr__(self):
        return "****"

# Load the secret key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the plain password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt the password and return a protected string
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)

# Final method to call from app
def get_decrypted_password():
    encrypted_password = b'gAAAAABpSlSxrX0_4bC2qjp3SH8K3pD-yYmNi_kqwoMFBNgoG-QGAVaw-Om0moIrPNLXWcW41RhSz2STWmuSijYxf8bfpCcbvA==' # 🔐 Paste the encrypted output here
    return decrypt_password(encrypted_password)