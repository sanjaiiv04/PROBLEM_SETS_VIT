#cyclic shift of characters of string
def shift(s):
    global a
    a=s[1:]+s[0]
    return a

s=input("enter a string:")
print(s)
for i in range(len(s)-1):
    print(shift(s))
    s=a
print('cyclic shift...')