def myfun(*argv):
    for arg in argv:
        print (arg)

myfun('hello', 'how ', 'are', 'you')

def myfun1(arg1, *argv):
    print("First argument :" ,arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myfun1("First", "second", "third", "fourth", "fifth")

#python to illustrate **kwargs 

def myfun3(**kwargs):
    for key,value  in kwargs.items():
        print( "%s == %s" %(key, value))

#Driver code
myfun3(first ="Sandeep" , last ="billakanti")

#**kargs for variable number of keyword arguments with one extra argument

def myfun4(arg1, **kwargs):
    for key,value in kwargs.items():
        print( "%s == %s" %(key, value))

#Driver code
myfun4("This is first argument", first = "Sandeep", last ="billakanti")
