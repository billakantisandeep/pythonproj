class emp:

    num_of_emp = 0
    raise_amt = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        emp.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod   #Using this class method as alternative constructer
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)



emp1 = emp('Sandeep', 'Billakanti', 20000)
emp2 = emp('Udvi', 'Billakanti', 30000)

#class methods used as constructers.
emp_str_1 = 'udvi-b-4000'
emp_str_2 = 'minnu-b-5000'
emp_str_3 = 'teju-b-6000'

new_emp_1 = emp.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.first)


