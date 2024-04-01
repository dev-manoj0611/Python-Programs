inp,l=int(input("Mention the number of elements you want to add : ")),[]
for i in range(1,inp+1):
    if i==1:
        inpu=input("Enter the {}st value : ".format(i))
    if i==2:
        inpu=input("Enter the {}nd value : ".format(i))
    if i==3:
        inpu=input("Enter the {}rd value : ".format(i))
    if i>3:
        inpu=input("Enter the {}th value : ".format(i))
    l.append(inpu)
tup=tuple(l)
print(tup)
for j in range(0,inp):
    print(tup[j])