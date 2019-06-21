from operator import attrgetter


class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('Udvi', 0.5, 100000000)
e2 = Employee('Teju', 28, 100000)
e3 = Employee('Sandeep', 31, 100)

employees = [e1,e2,e3]
# def e_sort(emp):
#     return emp.name

s_employees = sorted(employees, key=attrgetter('name'))  #Change name,age or any argument if you want to sort on that basis.
print(s_employees)
