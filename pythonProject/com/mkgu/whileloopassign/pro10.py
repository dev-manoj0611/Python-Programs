i = int(input('Enter a number to check whether it is prime or not : '))
j = 1
count = 0
while True:
    if j <= i:
        if i % j == 0:
            count += 1
        j += 1
    else:
        break
if count == 2:
    print(i, 'is prime')
else:
    print(i, 'is not prime')