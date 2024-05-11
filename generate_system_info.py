import os
import platform

def generate_system_info(directory):
    os.makedirs(directory, exist_ok=True)
    for i in range(10):
        with open(os.path.join(directory, f'file{i}.txt'), 'w') as file:
            file.write(f'System Information:\n{platform.uname()}')
generate_system_info('C:/Users/jrmed/Documents/Javascript')

