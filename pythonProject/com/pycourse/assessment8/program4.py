tup=(1,2,3,1,2,1,0,0,2)
a=list(tup)
b=[]
for i in range(0,9):
    count=a.count(a[i])
    if a[i] not in b:
        b.append(a[i])
        if(count>1):
            print(a[i]," is repeated ",count,"times")