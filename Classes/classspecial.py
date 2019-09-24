class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = init(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}, '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Sandeep', 'Billakanti', 10000)
emp_2 = Employee('Udvi', 'Billakanti', 2000000)

print(len('sandeep'))
print('sandeep'.__len__())

print(emp_1 + emp_2)  #Adding the employee salaries.

print(len(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a' ,'b'))


