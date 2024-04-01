d=True
while d==True:
    s=input("Enter the string containing minimum 4 words : ").split(" ")
    t=[]
    if len(s)>3:
        for i in range(len(s)):
            if i==1 or i%2==1:
                j=s[i]
                v=j[-1::-1]
                t.append(v)
            else:
                t.append(s[i])
        d=False
    else:
        print("***Minimum 4 words is expected in the string***")
        d=True
print(t)