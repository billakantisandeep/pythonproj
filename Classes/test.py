class Employee:
    def __init__(self,name,age,salary,last):
        self.name = name
        self.age = age
        self.salary = salary
        self.last = last 
    def fullname(self):
        return'{} {}'.format(self.name, self.last)
    
emp1 = Employee('Sandeep', 31, 1000, 'billakanti')
index = Employee.fullname(emp1)
print(index)