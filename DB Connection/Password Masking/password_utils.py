from cryptography.fernet import Fernet

# Class to prevent accidental print/log of password
class FakeStr(str):
    def __str__(self):
        return "****"

    def __repr__(self):
        return "****"

# Load the secret key
def load_key():
    return open("DB Connection/Password Masking/secret.key", "rb").read()

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
    encrypted_password = b'gAAAAABpbO4YlM5Qy_dRYIEtCT_o0n1EEtOBYs3_l-SunnKK5w33BMOn_S-0PYX94CgP4_zg0WWcvRbsXCEKz3fE32rO_b3rmg==' # 🔐 Paste the encrypted output here
    return decrypt_password(encrypted_password)