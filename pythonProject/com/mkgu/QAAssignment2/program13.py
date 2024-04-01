list2= [1, 2, 3, 4, 2, 6, 3]
dup=[]
for i in list2:
    if i in dup:
        print(i,"is repeated")
    else:
        dup.append(i)
if len(dup)==len(list2):
    print("there are no duplicate elements in list2")