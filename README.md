# Python File Encryptor

A simple and secure file encryption tool written in Python using AES-256-GCM with random key generation.

## Features

- AES-256-GCM encryption
- Random 256-bit key generation for each encryption
- Random nonce for each encryption
- Encrypted file and key file saved separately
- Works with any file type (txt, jpg, pdf, mp4, etc.)

## Installation

pip install cryptography

Or use requirements.txt:

pip install -r requirements.txt

## Usage

### Encrypt a file

from encryptor import encrypt_file

enc_file, key_file = encrypt_file(
    input_file_path="/path/to/your/file.txt",
    output_dir="/path/to/output/"
)
print("Encrypted file:", enc_file)
print("Key file:", key_file)

### Decrypt a file

from encryptor import decrypt_file

decrypt_file(
    encrypted_file_path="/path/to/output/file.txt.enc",
    key_file_path="/path/to/output/file.txt.key",
    output_path="/path/to/decrypted.txt"
)
print("Decrypted successfully!")

## Output Files

After encryption, two files are created:

- file.txt.enc - The encrypted file (contains nonce + ciphertext)
- file.txt.key - The encryption key (32 bytes, keep it safe!)

## Security Notes

- Keep the .key file safe! Without it, files cannot be recovered.
- Store the .key file separately from the .enc file.
- Delete the original file after encryption.

## Important: Change the Paths!

Before running the program, you MUST change the file paths in the code to match your system.

### Windows paths:

input_file_path = r"C:\\Users\\YourName\\Desktop\\secret.txt"
output_dir = r"C:\\Users\\YourName\\Desktop\\Folder"

### Linux/Mac paths:

input_file_path = "/home/username/Desktop/secret.txt"
output_dir = "/home/username/Desktop/Folder"

## License

MIT License