#encryption problem 
#creating a dict with alphabets as key 
#and their corresponding numbers as values
alpha=[chr(n) for n in range(65,91)]
digits=[n for n in range(1,27)]
dict_alpha=dict(zip(alpha,digits))
print(dict_alpha)

msg=input("enter msg:")
msg_encrypt=[]
for i in msg:
    msg_encrypt.append(dict_alpha[i]) 
#creating a list of the corresponding numbers of the letters of the message   

key=input("enter key:")
key_encrypt=[]
for i in key:
    key_encrypt.append(dict_alpha[i])

#creating a list of the corresponding numbers of the letters of the key

sum_encrypt=[]
for i in range(len(msg)):
    y=msg_encrypt[i]+key_encrypt[i]
    #adding the corresponding numbers of the message and key
    if y>26:
        y=y-26
    else:
        pass
    sum_encrypt.append(y)

k=list(dict_alpha.keys())
#getting the keys of the dict using the values from the sum_encrypt
for i in sum_encrypt:
    print(k[i],end='')