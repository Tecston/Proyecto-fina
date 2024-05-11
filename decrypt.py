import os
from cryptography.fernet import Fernet

def decrypt_files(directory, key):
    cipher_suite = Fernet(key)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            with open(os.path.join(directory, filename), 'rb') as file:
                decrypted_data = cipher_suite.decrypt(file.read())
            with open(os.path.join(directory, filename), 'wb') as file:
                file.write(decrypted_data)
            print(f"El archivo {filename} ha sido descifrado correctamente.")

key = b'vdPDkgx0oWHzyYF76j-MnjDQnvhSz7-hJfPYKbLYxTQ='
decrypt_files('C:/Users/jrmed/Documents/Javascript', key)
