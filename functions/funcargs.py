#this code illustrates sending the arguments to the function.

def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

# print(hello_func('HI', name='Sandeep'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math','Art', name='Sandeep', age=22)


#These two allows us to enter any no. of arguments of different types