#given n sequence of numbers
#remove first kth element and last kth element from the sequence 
#where k is given by k<=n/2 and and n>=10
l=list(map(int,input("enter numbers:").split()))
if len(l)>=10:
    k=len(l)//2
    for i in range(k):
        a=l[i+1:len(l)-i-1]
        if a!=[]:
            print(a)
        else:
            break
       