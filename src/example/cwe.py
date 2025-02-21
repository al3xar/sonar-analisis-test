import os
import sqlite3
import os
import subprocess
import hashlib




def divide(a, b):
    return a / b  # No verifica si b == 0 (CWE-20)

# Mal: No hay validación de entrada
user_input = input("Enter a command: ")
os.system(user_input)  # CWE-78

subprocess.run(user_input, shell=True)  # CWE-78



num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
print(divide(num1, num2))


filename = input("Enter the filename: ")  # CWE-22
with open(f"/var/www/{filename}", "r") as f:
    print(f.read())



conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Mal: Concatenación directa de entrada del usuario
user_input = input("Enter username: ")
query = f"SELECT * FROM users WHERE username = '{user_input}'"  # CWE-89
cursor.execute(query)


password = "mypassword"
hashed = hashlib.md5(password.encode()).hexdigest()  # CWE-327
print(hashed)