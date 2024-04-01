num1=int(input("Enter the number you wish to check whether is is prime or not: "))
if num1==1:
    print("Number is not a prime number")
elif num1>1:
    for i in range(2, int(num1/2)+1):
        if num1%i==0:
            print(num1, "is not a prime number")
            break
    else:
        print(num1, "is a Prime number")
else:
    print("Number is not a prime number")