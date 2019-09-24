try:
    f = open('C://Users/sbillakanti/pythonlearning/errors/test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

else:
    print(f.read())
    f.close()
finally:
    print("I am executing finally")   #Compulsory will be executed -- something like closing a database.