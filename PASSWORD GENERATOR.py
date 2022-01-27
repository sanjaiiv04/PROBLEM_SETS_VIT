#random password generator

import random 
import time

def gen_alpha(num):
    for i in range(num):
        password=''
        letter=[chr(random.randint(65,90)),chr(random.randint(97,122))]
        password+=random.choice(letter) #random.choice(list) chooses a random element from the list
        print(password,end='')

def gen_digit(num):
    for i in range(num):
        password=''
        letter=chr(random.randint(48,57))
        password+=letter
        print(password,end='')
        
def gen_alphadigit(num):
    for i in range(num):
        password=''
        letter=[chr(random.randint(65,90)),chr(random.randint(97,122)),chr(random.randint(48,57))]
        password+=random.choice(letter)
        print(password,end='')
        
def gen_mixed(num):
    for i in range(num):
        password=''
        letter=chr(random.randint(32,126))
        password+=letter
        print(password,end='')
        

print('========================PASSWORD GENERATOR==========================')
while True:
    n=int(input("ENTER THE NUMBER OF CHARACTERS FOR THE PASSWORD:"))
    print("1.ALPHABETIC PASSWORD")
    print("2.NUMERIC PASSWORD")
    print("3.ALPHANUMERIC PASSWORD")
    print("4.EXIT")
    ch=int(input("ENTER YOUR CHOICE:"))
    if ch==1:
        print("GENERATING A PASSWORD.......")
        time.sleep(4)
        print("YOUR PASSWORD:")
        gen_alpha(n)
        print('')
        print("==========================THANK YOU==========================")
    elif ch==2:
        print("GENERATING A PASSWORD.......")
        time.sleep(4)
        print("YOUR PASSWORD:")
        gen_digit(n)
        print('')
        print("==========================THANK YOU==========================")
    elif ch==3:
        print("GENERATING A PASSWORD.......")
        time.sleep(4)
        print("YOUR PASSWORD:")
        gen_alphadigit(n)
        print('')
        print("==========================THANK YOU==========================")
    elif ch==4:
        print('HAVE A NICE DAY!')
        break
    else:
        pass
        
    
        


