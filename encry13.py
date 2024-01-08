import random, string 

print('''                ███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗ ██╗██████╗ 
                ██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝███║╚════██╗
                █████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ╚██║ █████╔╝
                ██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝   ██║ ╚═══██╗
                ███████╗██║ ╚████║╚██████╗██║  ██║   ██║    ██║██████╔╝
                ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═╝╚═════╝ ''')

userchoice=input('''1.Encrypt Password:
2.Decrypt Password:
3.Exit                 
~ Enter your choice: ''')

def rotencrypt(inp):
   char_list=string.ascii_lowercase
   return "".join([char_list[(char_list.find(char) + 13) % 26] for char in inp]) 


def encryption():
    inp=input("Enter the Password(only characters & less than 8 characters):")
    rotinp=rotencrypt(inp)
    mylist=list(rotinp)
    fLetter=mylist[0] 
    mylist.pop(0)
    mylist.append(fLetter)

    special=string.ascii_letters + string.digits + string.punctuation 
    randcharFront=''.join(random.choice(special) for _ in range(8))
    randcharRear=''.join(random.choice(special) for _ in range(10)) 
    mylist=list(randcharFront) + mylist + list(randcharRear) #Grouping random chars and list in an list
    enc_str=''.join(mylist)    #converting list into an string by joining
    print("\nYour Encrypted Password is "+enc_str)
    print(f"Length of Password :{len(enc_str)}")

def decryption():
   inpdec=input("Enter your encrypted password: ")
   inppass=inpdec[8:-10]
   rtpass=(inppass[-1:]+inppass[0:-1])
   final_pass=rotencrypt(rtpass)
   print(f'Your Decrypted Password is {final_pass}')

match userchoice:
   case '1':
      encryption()
   case '2':
      decryption()
   case '3':
      exit()
   case _:
      print('Invalid Input')

