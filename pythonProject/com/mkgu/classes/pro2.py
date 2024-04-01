class Company:
    company = 'Western Digital'
    location = 'Bengaluru'

    def employee_attributes(self, empname, empid, empdesignation, empsalary):
        self.empname = empname
        self.empid = empid
        self.empdesignation = empdesignation
        self.empsalary = empsalary

    def employee_details(self):
        print('Company : ', self.company)
        print('Location : ', self.location)
        print('Employee name : ', self.empname)
        print('Employee id : ', self.empid)
        print('Employee designation : ', self.empdesignation)
        return 'Employee salary : {}'.format(self.empsalary)


empname = input('Enter the employee name : ')
empid = input('Enter the employee id : ')
empdesignation = input('Enter the employee designation : ')
empsalary = input('Enter the employee salary : ')

company_obj = Company()
company_obj.employee_attributes(empname, empid, empdesignation, empsalary)
print('The Employee details are : ')
print(company_obj.employee_details())
