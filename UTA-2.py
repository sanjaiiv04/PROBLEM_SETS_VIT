#pattern(uta-7)
'''for i in range(1,10):
    for j in range(i+1):
        c=i
        print(c,end='')
        c+=1
    print()'''


#print n fibonacci number where n is input  (uta-3) 
'''def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a,b=b,c


n=int(input("enter no:"))
fibonacci(n)'''


#union of two lists without union()
'''l1=eval(input("enter list1:"))
l2=eval(input("enter list2:"))
l1.extend(l2)
l3=[]
for i in l1:
    if i not in l3:
        l3.append(i)
print(l3)'''
    

#uta-1
'''l=[10,20,30,40,50,60]
pos=2
idx=0
while len(l)>0:
    idx=(pos+idx)%len(l)
    l.pop(idx)
    print(l)'''




































    