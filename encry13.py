import random
import string
import json
import os

# Get the directory of the current program(encry13)
curr_dir = os.path.dirname(os.path.abspath(__file__))
pass_file = os.path.join(curr_dir, "passwords.json") #stores the password file in the same encry13 directory

# ROT13 encryption function logic which allows to input upto 26 chars including special chars & symbols
def rotencrypt(inp):
    def rotate_char(c):
        if c.islower():
            return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        elif c.isdigit():
            return c  # Keep digits as they are
        else:
            # Keep special characters and spaces unchanged
            return c

    return ''.join(rotate_char(c) for c in inp)

#Encryption function for adding random chars with Rot13 encryption
def encrypt_password(password):
    rotinp = rotencrypt(password)
    mylist = list(rotinp)
    fLetter = mylist[0]
    mylist.pop(0)
    mylist.append(fLetter)

    special = string.ascii_letters + string.digits + string.punctuation
    randcharFront = ''.join(random.choice(special) for _ in range(8))
    randcharRear = ''.join(random.choice(special) for _ in range(10))
    mylist = list(randcharFront) + mylist + list(randcharRear)
    enc_str = ''.join(mylist)
    return enc_str

#Decryption function
def decrypt_password(encrypted_password):
    inppass = encrypted_password[8:-10]
    rtpass = (inppass[-1:] + inppass[:-1])
    final_pass = rotencrypt(rtpass)
    return final_pass

#Function for storing the username and password as key:value pair in the file
def store_password(account, encrypted_password):
    try:
        with open(pass_file, "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    passwords[account] = encrypted_password

    with open(pass_file, "w") as file:
        json.dump(passwords, file)

#Function which will retrieve the password as per the username
def retrieve_password(account):
    try:
        with open(pass_file, "r") as file:
            passwords = json.load(file)
            encrypted_password = passwords.get(account)
            if encrypted_password:
                return encrypted_password
            else:
                print("No password found for that account.")
                return None
    except FileNotFoundError:
        print("No passwords stored yet.")
        return None

#Main Menu
def encry_main():
    print('''                ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗ ██╗██████╗
                ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝███║╚════██╗
                █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ╚██║ █████╔╝
                ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝   ██║ ╚═══██╗
                ███████╗██║ ╚████║╚██████╗██║  ██║   ██║    ██║██████╔╝
                ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═════╝
                                @iazimshaikh (Azim Shaikh)''')

    while True:
        choice = input('''\n1. Encrypt and Store Password
2. Retrieve Password
3. Exit
~ Enter your choice: ''')

        if choice == '1':
            account = input("Enter the username of account(any social media account): ")
            password = input("Enter the password to encrypt and store in a file (up to 26 characters, including spaces and special characters): ")
            if len(password) > 26:
                print("Password must be 26 characters or less. Please try again.")
                continue
            encrypted_password = encrypt_password(password)
            store_password(account, encrypted_password)
            print("Password stored successfully!")

        elif choice == '2':
            account = input("Enter the account name to retrieve the password: ")
            encrypted_password = retrieve_password(account)
            if encrypted_password:
                decrypted_password = decrypt_password(encrypted_password)
                print(f"Password for {account}: {decrypted_password}")

        elif choice == '3':
            exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    encry_main()
