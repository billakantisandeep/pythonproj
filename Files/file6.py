#Write to a file
#Using the context managers

with open('C:\\Users\\sbillakanti\\pythonlearning\\Files\\test1.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Rest')













#If the file doesnt exist it will create it.
#if the file exists then append dont use the write
#Use pass to just create without writing anything.