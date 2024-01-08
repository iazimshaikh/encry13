# Password Encryption and Decryption

This Python script allows you to encrypt and decrypt passwords using a simple rotation cipher with a random special character mix using rot13 encryption technique.

## Usage

1. **Encrypt Password:**
   - Select option `1` to encrypt a password.
   - Enter a password containing only characters and less than 8 characters.
   - The script will generate an encrypted password with a random mix of special characters.

2. **Decrypt Password:**
   - Select option `2` to decrypt an encrypted password.
   - Enter the encrypted password when prompted.
   - The script will decrypt the password and display the original text.

3. **Exit:**
   - Select option `3` to exit the program.

## How it Works

- The script uses a rotation cipher (Caesar cipher with a rotation of 13) to encrypt the input password.
- For encryption, it adds random special characters at the beginning and end of the encrypted password.
- For decryption, it reverses the process by removing the added special characters and then decrypting the password.

## Getting Started

1. Clone the repository and ready to go:
   ```bash
   git clone https://github.com/thecyberkings/encry13.git
   cd your-repository
   python encry13.py

## Note
This script is a simple example and may not provide strong security. It is intended for educational purposes.
Ensure you have Python installed on your system before running the script.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

Happy Coding! 🚀
