read=input("Enter a string to check whether it is a palindrome : ")
isPalindrome=read[::-1]
print(isPalindrome)
if isPalindrome==read:
    print("String",read,"is a palindrome")
else:
    print("String",read,"is not a palindrome")