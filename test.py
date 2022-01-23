def max(l):
    cnt=0
    key=l[0]
    for i in range(len(l)-1):
        try:
            if key > l[i+1]:
                cnt=1
            else:
                cnt=0
                key=l[i+1]
                
        except IndexError:
            print('reached the end of the array..')
    print ('maximum element of the array:',key)

#main
l=list(map(int,input('enter space separated list elements:').split()))
max(l)
