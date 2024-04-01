class Student:
    def __init__(self, internals, externals):
        self.internals = internals
        self.externals = externals

    def __add__(self, other):
        stu1total = self.internals + other.internals
        stu2total = self.externals + other.externals
        return stu1total + stu2total


stu1_obj = Student(55, 65)
stu2_obj = Student(88, 55)
print(stu1_obj + stu2_obj)