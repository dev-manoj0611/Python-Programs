i = int(input('Enter a number to check whether is is prime or not: '))
if i == 1:
    print(i, 'is not a prime number')
elif i > 1:
    j = 2
    while j in range(2, int(i / 2) + 1):
        if i % j == 0:
            print(i, 'is not a prime number')
            break
        j += 1
    else:
        print(i, 'is a prime number')
else:
    print(i, 'is not a prime number')
