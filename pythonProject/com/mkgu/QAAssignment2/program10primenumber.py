# list7=[2,3,6,4,7,5,9,11,22,14,13,19,21,29,31,33]
# list8=[]
# p=len(list7)
# for x in range(list7[0],list7[p-1]):
#     count=0
#     z=x+1
#     for y in range(1,z):
#         if x%y==0:
#             count=count+1
#     if count==2:
#         list8.append(x)
# print(list8)
read=int(input("Enter an integer to find all the prime numbers below it : "))
count=0
for x in range(2,read+1):
    count=0
    z=x+1
    for y in range(1,z):
        if x%y==0:
            count+=1
    if count==2:
        print(x,"is prime")