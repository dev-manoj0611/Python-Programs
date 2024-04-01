tup=('m','a','n','o','j','k','u','m','a','r')
a=list(tup)
user=input("Please enter an element to check its existence in the tuple : ")
if user in a:
    print("Element ",user," exists in tuple")
else:
    print("Element ",user," does not found")