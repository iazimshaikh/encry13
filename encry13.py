import random
import string
import json
import os

# ROT13 encryption function
def rotencrypt(inp):
    char_list = string.ascii_lowercase
    return "".join([char_list[(char_list.find(char) + 13) % 26] for char in inp])

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

def decrypt_password(encrypted_password):
    inppass = encrypted_password[8:-10]
    rtpass = (inppass[-1:] + inppass[:-1])
    final_pass = rotencrypt(rtpass)
    return final_pass

# Store passwords in a file
def store_password(account, encrypted_password):
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    passwords[account] = encrypted_password

    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Retrieve a password
def retrieve_password(account):
    try:
        with open("passwords.json", "r") as file:
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

def main_menu():
    print('''                ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗ ██╗██████╗
                ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝███║╚════██╗
                █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ╚██║ █████╔╝
                ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝   ██║ ╚═══██╗
                ███████╗██║ ╚████║╚██████╗██║  ██║   ██║    ██║██████╔╝
                ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═════╝ ''')
    while True:
        choice = input('''\n1. Encrypt and Store Password
2. Retrieve Password
3. Exit
~ Enter your choice: ''')

        if choice == '1':
            account = input("Enter the username of account(any social media account): ")
            password = input("Enter the password to encrypt and store in a file(only characters & less than 8 characters): ")
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
    main_menu()
