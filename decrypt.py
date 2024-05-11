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

key = b's_IcXV3ylUAfv4T-AkXOaV-is7loNwh8aTZN_4T4ABk='
 
decrypt_files('C:/Users/jrmed/Documents/Javascript', key)
 
