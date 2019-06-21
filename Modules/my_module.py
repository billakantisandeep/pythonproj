print('Imported my_module')

test = 'Test String'

def find_index(to_search, target):
    ''' Find the index of a value in a sequence '''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1

class test1:
        def __init__(self,name,last):
                self.name =  name
                self.last = last

        def fullname(self):
                return '{} {}'.format(self.name, self.last)

index = test1('sandeep', 'billakanti')
print(test1.fullname(index))