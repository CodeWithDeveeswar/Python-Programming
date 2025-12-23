import mysql.connector
from password_utils import get_decrypted_password

def connect_to_mysql():
    conn = mysql.connector.Connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="test" # Change to your DB name if needed
    )
    print("✅ Connected to MySQl successfully")
    print(get_decrypted_password())
    conn.close()

if __name__ == "__main__":
    connect_to_mysql()