read=input("Enter a string containing at least 3 words : ").split()
if len(read)>=3:
    print(read)
else:
    print("Minimum 3 words are expected")