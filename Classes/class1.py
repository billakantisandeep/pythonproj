#OOPS in python


class Employee:
    # pass                            #To put the class empty for now 
    def  __init__(self, first, last, pay):              #By convention we use the first argument as self 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

# print('{} {}'.format(emp1.first, emp1.last))

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('sandeep', 'billakanti', 1000)
emp2 = Employee('medhamsh', 'vutpala', 1000)

print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
