#Python OOPS

class Employee:
#    pass #To leave the class empty
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

  #These are the instances of the classes that are defined.

emp1 = Employee('sandeep', 'billakanti', '3000')
emp2 = Employee('Udvi', 'billakanti', '3000')

#print(emp1.first)
#print(emp2.first)

#print('{} {}'.format(emp1.first, emp1.last))  #This is used for the full name but instead of this we can define a method in the class
#print(emp1.fullname())
#print(emp2.fullname())
print(emp1.fullname())  #this is calling instancce and method we dont need to call self
print(Employee.fullname(emp1)) #Running the methods using the class name -- Instance is being passed as self
print(Employee.fullname(emp2))

#Methods are having self if we do print(emp1.fullname()) in the background it will be converted to Employee.fullname(emp1)
# We need to clearly observe when the instance and method are called , when it is called using the class name.

