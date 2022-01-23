#finding leaders in an array
n=int(input("enter no of elements:"))
l=[]
a=0
for i in range(n):
    inp=int(input("enter no:"))
    l.append(inp)

for i in range(len(l)):
    try:
        if l[i]> l[i+1]:
            a=1
            print(l[i])
        else:
            a=0
    except IndexError:
        if a==0:
            print("no leaders")