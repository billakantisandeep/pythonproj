#This program is for the large and extremely large files to read the contents of the file

with open('C:\\Users\\sbillakanti\\pythonlearning\\Files\\test.txt', 'r') as f:
    f_contents = f.read(100)   #Prints the no. of characters
    print(f_contents, end='')   #this reads the entire contents of the file.

    f_contents = f.read(100)   #This prints the next hundred characters where it had left off.
    print(f_contents, end='')
# So printing the characters using the read method, how are we gonna use for a large file. Go to file3.py


    # for line in f:
    #     print(line, end = '')
    # f_contents = f.readline()
    # print(f_contents, end = '')

    # f_contents = f.readline()
    # print(f_contents, end = '')





#f.readlines()  -- This function gives the details of all the file.
#f.readline() -- gives the single line
#print(f_contents, end = '')  -- This will print without the extra line after each line.
#Use the for loop for no getting the memory issues using readline multiple times.
# for line in f:
#         print(line, end = '')
