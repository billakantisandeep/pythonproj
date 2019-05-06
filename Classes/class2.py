class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Sandeep', 'Billakanti', 10000)
emp_2 = Employee('Medhamsh', 'Vutpala', 200000)

print(Employee.fullname(emp_1))

