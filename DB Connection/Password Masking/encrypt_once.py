from password_utils import encrypt_password
from cryptography.fernet import Fernet

# Generate key and save to file
def generate_key():
    key = Fernet.generate_key()
    with open("DB Connection/Password Masking/secret.key", "wb") as f:
        f.write(key)
    print("✅ Key saved to 'secret.key'")

if __name__ == "__main__":
    # Uncomment if running for the first time
    # generate_key()

    # Replace with your real MySQL root password
    encrypted = encrypt_password("root")
    print("🔐 Encrypted password (copy this to password_utils.py):")
    print(encrypted)