list1= [1, 2, 3, 4, 1, 6, 3]
list2= [1, 2, 3, 4, 2, 6, 3]
for i in list1:
    if i in list2:
        continue
    else:
        print("all the elements in list1 are not included in list2")
        break
print("all the elements in list1 are included in list2")