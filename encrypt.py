import os
from cryptography.fernet import Fernet

def encrypt_files(directory, key):
    cipher_suite = Fernet(key)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            with open(os.path.join(directory, filename), 'rb') as file:
                encrypted_data = cipher_suite.encrypt(file.read())
            with open(os.path.join(directory, filename), 'wb') as file:
                file.write(encrypted_data)

key = Fernet.generate_key()
print(key)
encrypt_files('C:/Users/jrmed/Documents/Javascript', key)
