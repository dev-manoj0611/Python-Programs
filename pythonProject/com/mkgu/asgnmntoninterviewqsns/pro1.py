read = int(input('Enter a number to check whether it is prime or not : '))
i = 1
count = 0
if read == 1:
    print(read, 'is not prime')
else:
    while i in range(1, int(read / 2) + 1):
        if read % i == 0:
            count += 1
        i += 1
    if count == 1:
        print(read, 'is prime')
    elif count > 1:
        print(read, ' is not prime')
# num=int(input("enter the number :"))
# i=2
# if num==1:
#     print(num," is not a prime number")
# else:
#     while i<int(num/2)+1:
#         if num%i==0:
#             print(num," is not a prime number")
#             break
#         i+=1
#     else:
#         print(num," is a prime number")
