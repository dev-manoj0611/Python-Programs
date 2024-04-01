l=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
m=[]
for i in range(len(l)):
    ele=list(l[i])
    ele[2]=100
    ele=tuple(ele)
    m.append(ele)
print(m)