tup=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
l=list(tup)
l2=[]
for i in range(len(l)):
    c=list(l[i])
    avg = 0
    for j in range(len(c)):
        avg+=c[j]/len(c)
    l2.append(avg)
print(l2)