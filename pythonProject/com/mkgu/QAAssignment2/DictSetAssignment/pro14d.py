name=input("enter the name: ")
reg_no=int(input("enter the reg no:"))
social_marks=int(input("enter the social marks:"))
science_marks=int(input("enter the science marks:"))
maths_marks=int(input("enter the maths marks:"))
dict1={name:{reg_no:{'social':social_marks,'science':science_marks,'maths':maths_marks}}}
print(dict1)
name2=input("enter the name: ")
reg_no2=int(input("enter the reg no:"))
social_marks2=int(input("enter the social marks:"))
science_marks2=int(input("enter the science marks:"))
maths_marks2=int(input("enter the maths marks:"))
dict2={name2:{reg_no2:{'social':social_marks2,'science':science_marks2,'maths':maths_marks2}}}
print(dict2)
name3=input("enter the name: ")
reg_no3=int(input("enter the reg no:"))
social_marks3=int(input("enter the social marks:"))
science_marks3=int(input("enter the science marks:"))
maths_marks3=int(input("enter the maths marks:"))
dict3={name3:{reg_no3:{'social':social_marks3,'science':science_marks3,'maths':maths_marks3}}}
print(dict3)
print("************max marks in social***************")
if dict1[name][reg_no]['social']>dict2[name2][reg_no2]['social']:
    if dict1[name][reg_no]['social']>dict3[name3][reg_no3]['social']:
        print(dict1)
elif dict1[name][reg_no]['social']<dict2[name2][reg_no2]['social']:
    if dict2[name2][reg_no2]['social']>dict3[name3][reg_no3]['social']:
        print(dict2)
    else:
        print(dict3)
print("**************max marks in science*************")
if dict1[name][reg_no]['science']>dict2[name2][reg_no2]['science']:
    if dict1[name][reg_no]['science']>dict3[name3][reg_no3]['science']:
        print(dict1)
elif dict1[name][reg_no]['science']<dict2[name2][reg_no2]['science']:
    if dict2[name2][reg_no2]['science']>dict3[name3][reg_no3]['science']:
        print(dict2)
    else:
        print(dict3)
print("***************max marks in maths***************")
if dict1[name][reg_no]['maths']>dict2[name2][reg_no2]['maths']:
    if dict1[name][reg_no]['maths']>dict3[name3][reg_no3]['maths']:
        print(dict1)
elif dict1[name][reg_no]['maths']<dict2[name2][reg_no2]['maths']:
    if dict2[name2][reg_no2]['maths']>dict3[name3][reg_no3]['maths']:
        print(dict2)
    else:
        print(dict3)