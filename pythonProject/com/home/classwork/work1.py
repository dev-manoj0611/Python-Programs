# list1=[1,2,[3,4]]
# list2=list1[:]
# print(list1, list2)
# print(id(list1))
# print(id(list2))
# list1=[2,3,4]
# print(list1, list2)

# list1=['a','b',['c','d']]
# list2=list1[:]
# print(id(list1), id(list2))
# print(id(list1[0]), id(list2[0]))
# print(id(list1[1]), id(list2[1]))
# print(id(list1[2]), id(list2[2]))
# del list1[0]
# print(list1)
# print(list2)

list1=[1,2,[3,4]]
list2=list1
print(list1, list2)
list1[2]=9
print(list2)