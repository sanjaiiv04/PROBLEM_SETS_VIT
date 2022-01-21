

#converting binary into decimal(UTA-4)
'''t=input("enter a binary value:")
n=len(t)
res=0
for i in range(n,0,-1):
    res+=int(t[i-1])*(2**(n-i))

print('THE DECIMAL VALUE OF',t,':',res)'''

#logical and on two tuples of same size
'''t1=(0,1,0,1,1,0)
t2=(1,1,0,0,1,0)
t=()
for i in range(len(t1)):
    res=t1[i] and t2[i]
    t=t+(res,)
    
print(t)'''

#given n tuple as input, get maximum of each tuple and store in a new list.
'''n=int(input("enter number of tuples:"))
l=[]
l1=[]
for i in range(n):
    t=eval(input("enter tuple:"))
    l.append(t)
    max_t=max(t)
    l1.append(max_t)

print(l1)'''

#pariwise addition of tuple elements
'''t=(1,5,7,8,10)
t1=()
for i in range(len(t)):
    try:
        res=t[i]+t[i+1]
    except IndexError:
        break
    
    t1+=(res,)

print(t1)'''

# Python program to perform tuple intersection(order irrespective)
'''myTupleList1 = [(3,4), (5, 6)]
myTupleList2 = [(5,4), (4,3)]
print("Tuple List 1 : " + str(myTupleList1))
print("Tuple List 2 : " + str(myTupleList2))
intersection = set([tuple(sorted(vals)) for vals in myTupleList1]) & set([tuple(sorted(vals)) for vals in myTupleList2]) 
print("Intersection of both list : " + str(intersection))'''





