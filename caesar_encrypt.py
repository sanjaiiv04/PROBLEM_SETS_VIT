#caesar encryption
import string
def encrypt(l,k):
    l_new=[]
    chr=[i for i in string.ascii_lowercase]
    for i in l:
            x=(chr.index(i)+k)%26
            l_new.append(chr[x])
    for i in l_new: print(i,end='')

s=input("enter a string:")
k=int(input("enter the number of alphabets to jump:"))
l_string=[i for i in s]
encrypt(l_string,k)