list1=[0, 9, 2, 4, 5, 6]
list2=[]
for i in list1:
    if i%2==1:
        list2.append(i)
greatestOdd=max(list2)
print("greatest odd number in list1 is",greatestOdd)