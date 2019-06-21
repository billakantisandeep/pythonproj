#File Objects
f = open("C:\\Users\\sbillakanti\\pythonlearning\\Files\\test.txt", 'r')

print(f.name)
print(f.mode)

f.close()               #If you dont close the file, you will runout of ulimit value of no.of files to be opened in Os