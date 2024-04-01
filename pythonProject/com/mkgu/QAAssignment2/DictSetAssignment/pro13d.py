#Student Name, Reg No., Science, social, maths marks
s_data=[]
d_key=set()
d_value=set()
lis=[]
for i in range(1,3):
    s_data=[]
    name=input("Enter student name : ")
    s_data.append(name)
    regNo=int(input("Enter reg no. : "))
    s_data.append(regNo)
    sciMarks=int(input("Enter science marks : "))
    s_data.append(sciMarks)
    socialMarks=int(input("Enter social marks : "))
    s_data.append(socialMarks)
    mathsMarks=int(input("Enter maths marks : "))
    s_data.append(mathsMarks)
    d={s_data[0]:{s_data[1]:{s_data[2],s_data[3],s_data[4]}}}
    d_key = d_key.add(d.keys())
    #d_value = d_value.update(d.values())
print(d_key)
print(d_value)