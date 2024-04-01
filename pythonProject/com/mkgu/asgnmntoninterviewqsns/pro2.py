m = int(input('Enter a number a : '))
n = int(input('Enter a number b : '))
print('Prime numbers between',m,'and',n,'are : ')
if m == 1:
    m += 1
i = m
while i in range(m, n + 1):
    j = 2
    while j in range(2, int(i / 2) + 1):
        if i % j == 0:
            break
        j += 1
    else:
        print(i, 'is prime')
    i += 1
# 1. Find a given number is prime or not? using while loop only
# 2. Print all the prime numbers between the range 1 to 100? using a while loop only
# 3. Find all the numbers between the range 1 to 100 which are divisible by 9? using while loop
# 4. Find the minimum number in the list without using min() and by using a while loop?
# 5. Take a list ie; list1=[100, 70, 3, 20, 8, 9, 10] and sort list in reverse order without using sort()?
# 6. Take random elements from the user for a list with length 5 and sort the list in reverse order without using sort()?
# 7. Write a program to find the smallest number among 3 given numbers? Take 3 numbers input from the user?
