# Password Encryption and Decryption

This Python script allows you to securely store and retrieve passwords for your social media accounts using a custom encryption method based on the ROT13 technique combined with random special characters.

## Features

1. **Store Passwords:** Encrypt and save passwords for various accounts.
2. **Retrieve Passwords:** Decrypt and display stored passwords when you forgot your password for your account.


## Usage

1. **Encrypt Password:**
  - Select option `1` from the main menu.
  - Enter the account name (e.g., any username which you have used at the time of encryption , ex-"myinstagram").
  - Enter the password to encrypt (only characters, less than 8 characters).
  - The script will generate an encrypted password and store it.


2. **Decrypt Password:**
  - Select option `2` from the main menu.
  - Enter the account name for which you want to retrieve the password (ex-"myinstagram").
  - The script will display the decrypted password.

3. **Exit:**
   - Select option `3` to exit the program.

## How it Works

The script employs a custom encryption method:

**Encryption:** It uses the ROT13 technique to obfuscate the password and adds random special characters at the beginning and end for added complexity.
**Decryption:** The process is reversed by removing the added characters and applying ROT13 to recover the original password.

All passwords are stored in a JSON file, allowing for easy retrieval.

## Getting Started

1. Clone the repository and ready to go:
   ```bash
   git clone https://github.com/iazimshaikh/encry13.git
   cd your-repository
   python encry13.py

## Note
This script is a simple implementation of password storage and retrieval using custom encryption. While it provides a basic level of security, it is not suitable for protecting highly sensitive information(can use individually/personally for your socail media accounts). It is intended for educational purposes and personal use.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

Happy Coding! 🚀
