#This program demonstrates the closing of the file without using the f.close()
#Using the context managers -- Which will help inclosing
#Within the context manager

with open('C:\\Users\\sbillakanti\\pythonlearning\\Files\\test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)


print(f.name)    #To open the file name
# print(f.read())  #It gives error since we need to work within the with(Block)


#Reading from the file
#You can use the  print(f.read()) method to read the contents but it would be better to take in a variable so that you can work on that.