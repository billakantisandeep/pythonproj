class emp:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{}{}'.format(self.first, self.last)


emp_1 = emp('Sandeep', 'Billakanti', 50000)
emp_2 = emp('Test' ,'user', 20000)

# print(emp_1.fullname())
print(emp.fullname(emp_1))

print(emp_1.email)

