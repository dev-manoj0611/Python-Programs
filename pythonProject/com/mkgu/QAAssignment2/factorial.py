read=int(input("Enter an integer input to obtain its factorial : "))
prod=1
for i in range(1,read+1):
    prod=prod*i
print("factorial of",read,"is",prod)