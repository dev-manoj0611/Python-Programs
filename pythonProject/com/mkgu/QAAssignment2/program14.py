list1= [1, 2, 3, 4, 5, 6, 7]
list2= [1, 2, 3, 4, 2, 6, 3]
for i in list1:
    if i in list2:
        print(i,"is present in both list1 and list2")