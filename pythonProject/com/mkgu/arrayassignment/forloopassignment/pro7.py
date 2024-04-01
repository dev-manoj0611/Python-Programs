read = input("Enter a string : ")
if read == read[::-1]:
    print(read, 'is palindrome')
else:
    print(read, 'is not a palindrome')