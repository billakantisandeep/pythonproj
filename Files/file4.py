#Program to demonstrate read method of reading no. of characters for a larger file.
#Using Context managers. 
with open('C:\\Users\\sbillakanti\\pythonlearning\\Files\\test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f.tell())   #This gives the position 10

    while len(f_contents) > 0:
        print(f_contents, end = '*')
        f_contents = f.read(size_to_read)  #If you dont give this it does a infinte loop




#When we hit the end of the read it returns nothing