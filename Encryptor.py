import os
# For working with files and folders
import secrets
# For making random codes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_file(input_file_path, output_dir):
    with open(input_file_path , 'rb') as f:
        plaintext = f.read()

    key = AESGCM.generate_key(bit_length=256)
# Make a new random password (32chracters long ) 
    nonce = secrets.token_bytes(12)
# Make a random code (12 characters) that is diffrent evry time   
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
# Look that file! Change it to secret code
    encrypted_data = nonce + ciphertext
# Put the random code at the start of loked file (we need it later)
    base_name = os.path.basename(input_file_path)
    encrypted_file_path = os.path.join(output_dir, f"{base_name}.enc")
    key_file_path = os.path.join(output_dir, f"{base_name}.key")
    
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    
    with open(key_file_path, 'wb') as f:
        f.write(key)
    
    return encrypted_file_path, key_file_path


def decrypt_file(encrypted_file_path, key_file_path, output_path):
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    
    with open(key_file_path, 'rb') as f:
        key = f.read()
    
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]
    
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
# Unlock the file! Change secret code back to orginal
    with open(output_path, 'wb') as f:
        f.write(plaintext)
    
    return output_path


if __name__ == "__main__":
    
    enc_file, key_file =encrypt_file(
        input_file_path=r"C:\Users\Administrator\Desktop\secret.txt",
        output_dir=r"C:\Users\Administrator\Desktop\Folder"
    )
    
    print("the file was locked:", enc_file)
    print("file key:", key_file)
    
    decrypt_file(
        encrypted_file_path=r"C:\Users\Administrator\Desktop\Folder\secret.txt.enc",
        key_file_path=r"C:\Users\Administrator\Desktop\Folder\secret.txt.key",
        output_path=r"C:\Users\Administrator\Desktop\output.txt"
    )
    
    print("the file opened",r"C:\Users\Administrator\Desktop\output.txt")