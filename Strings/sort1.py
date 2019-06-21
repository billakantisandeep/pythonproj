# li = [-6, -5,-4,1,2,3]
# print(li)
# s_li = sorted(li, key=abs)  #key is very important 
# print('Sorted list:\t', s_li)


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
def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)
print(s_employees)
