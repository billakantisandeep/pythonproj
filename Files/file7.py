

with open('C:\\Users\\sbillakanti\\pythonlearning\\Files\\test.txt', 'r') as rf:   #Open a file to read
    with open('C:\\Users\\sbillaknati\\pythonlearning\\Files\\test1_copy.txt', 'w') as wf:    #Write the contents of that file into newone.
        for line in rf:
            wf.write(line)


