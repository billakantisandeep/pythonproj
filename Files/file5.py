#This program is for listing 10 characters of the file and using seek function to start over again
#using the context manager

with open('C:\\Users\\sbillakanti\\pythonlearning\\Files\\test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, '')

    f.seek(0)   #This will set the position to back to beggining of the file. You can use to any position.

    f_contents = f.read(size_to_read)
    print(f_contents)

