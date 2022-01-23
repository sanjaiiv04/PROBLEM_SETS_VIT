
#eligibility for scholarship

'''grad=input("ARE YOU FIRST GRADUATE IN YOUR FAMILY?(Y/N):")
if grad=='y':
    maths=float(input("enter your maths marks:"))
    phy=float(input("enter your physics marks:"))
    chem=float(input("enter your chemistry marks:"))
    if (maths and phy and chem)>0:
        avg=(maths+chem+phy)/3
        print("your average is:",avg)
        if avg>98:
            print("you are eligible")
        else:
            print("sorry you are not eligible")
    else:
        print("invalid")
        
else:
    print("you are not a first graduate.")'''


#leap year

'''yr=int(input("enter the year:"))
if yr%4==0:
    print("it is a leap year")
else:
    print("not a leap year")'''


# finding roots of quadratic equation
'''import math
print("consider the quadratic equation be:ax^2+bx+c=0")
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
d=b**2-(4*a*c)
x1=(-b+(math.sqrt(d)))/2*a
x2=(-b-(math.sqrt(d)))/2*a
print("the roots of the equation are:",int(x1),int(x2))'''

    


# class average by n students
'''n=int(input("enter no of students:"))
i=0
total=0
while i<n:
    marks=float(input("enter total mark of the student:"))
    total+=marks
    i+=1
    

avg=total/n
print("average of all students:",'{:.2f}'.format(avg))'''


#browsing centre

'''n_hrs=int(input("enter no of hrs:"))
n_mins=int(input("enter no of mins:"))
if n_hrs<7:
    if n_hrs>=5:
        print(200+(n_hrs-5)*50+(n_mins*1))
    else:
        print(n_hrs*50+n_mins*1)
else:
    print("you have exceeded the limit")'''


#left multiple 4 digit number

'''n=int(input("enter a 4 digit number:"))
num=str(n)
first_two_digit=int(num[0:2])
second_two_digit=int(num[2:4])
if (first_two_digit) % (second_two_digit)==0:
    print('yes it is a left multiple number')
else:
    print('no it is not a left multiple number')'''


#prime number

'''n=eval(input("enter a number:"))
if type(n)!=int:
    print("the number should be an integer!!")
else:
    lim=int(n/2)+1
    for i in range(2,lim):
        if n%i==0:
            print("composite")
            break
    else:
        print("prime")'''



#1 get a group of 5 numbers and another input no and find if the numbers in the group are divisible by that input number
'''l=[]
n=int(input("enter number to divide with:"))
for i in range(5):
    a=int(input("enter no:"))
    l.append(a)

for i in l:
    if i%n==0:
        print(i)
    else:
        continue'''
    
    
#2-factorial of a number
'''n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
        fact=fact*i
print(fact)'''

#4multiples of an odd number

'''n=int(input("enter a number:"))
if n%2!=0:
        for i in range(n,100,n):
                print(i)
else:
        print("its even")'''

#list comprehensions
'''def pow(n):
    return n**n

res=map(pow,[1,2,3,4])''' #map is an inbuilt function used to apply a function to every element of an iterable list/tuple and return the result in a list.
'''print(list(res))
print(res)''' #printing the result without list() will give a map object of the variable.


#printing pattern using nested for loop
'''n=int(input("enter number of steps:"))
for i in range(n):
    for j in range(i):
        print('*',end='')
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print('')'''

#printing a matrix of order i X j with nested for loop
'''n1=int(input("enter no of rows:"))
n2=int(input("enter no of columns:"))
l1=[]
l2=[]
for i in range(n1):
    for j in range(n2):
        mat=int(input("enter elements of matrix:"))
        l1.append(mat)
        
l2.append(l1)
print(l2)'''

#finding maximum occurence of an element in a list. if two numbers have same occurence print the highest among them
'''l=eval(input('enter a list:'))
d={}
l_keys=[]
l_values=[]
for element in l:
    if element in d:
        d[element]+=1
    else:
        d[element]=1
for i in d:
    print(i,':',d[i])'''


#given two keys k1,k2 as input print all the elements between them in a list(where k1<=x<=k2 ; x is the element to be printed)    
'''k1=int(input("enter the first key:"))
k2=int(input("enter the second key:"))
l=eval(input("enter the list:"))
if k1 and k2 in l:
    a=l.index('k1')
    b=l.index('k2')
    for i in range(a,b+1):
        print(l[i],end=',')
        
elif k1 not in l or k2 not in l:
    print("sorry")'''


#given a list of n integers, find if the list contains two numbers whose sum is equal to an arbitary integer k.
'''l=eval(input('enter a list:'))
k=int(input("enter the arbitary integer:"))
a=0
for i in l:
    for j in l:
        if i+j==k:
            a+=1

if a>0:
    print('yes')'''


# PAT-1
'''n=int(input('enter number of units:'))
res=0
if n>=1 and n<=100:
    res=res+(n*1.5)+25
    print(res)

elif n>=101 and n<=200:
    res=res+(100*1.5)+((n-100)*2.5)+50
    print(res)

elif n>=201 and n<=300:
    res=res+(100*1.5) + (100*2.5) + ((n-200)*4)+75
    print(res)

elif n>=301 and n<=350:
    res=res+(100*1.5)+(100*2.5)+(100*4)+((n-300)*5)+100
    print(res)
elif n>350:
    res=1500
    print(res)'''
    
#removing all occurence of an item from a list
'''l=[1,2,3,4,2]
res=[]
n=int(input("enter the number you want to erase:"))

for i in range(len(l)):
    if l[i]==n:
        continue
    else:
        res.append(l[i])
print(res)'''

#counting unique elements in a list
'''l=[1,1,2,2,3]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(len(l1))'''

#given a list of list of 2 numbers convert them into a list of numbers
'''l=[[1,2],[3,4],[10,5],[6,9]]
l1=[]
q=0
for i in l:
    for j in i:
        q=i[0]*i[1]
    l1.append(q)
print(l1)'''

#pattern question
'''n=int(input("enter a number:"))
for i in range(n):
    c=1
    for j in range(i+1):
        print(c,end='')
        c=c+1
        
    print()
for i in range(n,0,-1):
    d=1
    for j in range(1,i):
        print(d,end='')
        d=d+1
    print()'''

 
#dividing string into substrings of length k and removing duplicates in those substrings
'''s=input("enter string:")
k=int(input("enter number:"))
l=[]
for i in range(0,len(s)-2):
    l.append(s[i*k:k+i*k])
print(l)
print("Removing duplicates from the substrings...")
for i in l:
    s=''
    for j in i:
        if j not in s:
            s=s+j
    print(s)'''



    





        
