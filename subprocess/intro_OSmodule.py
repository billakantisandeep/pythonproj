import os

#print(dir(os))   #Prints all the attributes and variables.

print(os.getcwd())  #Printing the current working directory
#os.chdir('C:\Users\sbillakanti\')  #For changing the current working directory to the specified one. 
#print(os.listdir())     #List all the files in the folder
# os.mkdir('Os-demo-1')    #Create the directory in the current folder 
# os.makedirs('os-demo-2/os-sub-1')   #Creating the progressive directories like mkdir -p
# os.removeddirs('os-demo/os-demo1')  #Remove the dir and underlying directories 
# os.rename('text.txt', 'newtxt.txt')  #To rename the directory
# print(os.stat('demo.txt'))   #gives the stats like size 
# print(os.stat('demo.txt').st_creator)  #Gives the name of the creater 
# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))   #For seeing the human readable timestamp
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):  #To get the directories and files. 
    # print('Current Path:', dirpath)
    # print('Directories:', dirnames)
    # print('Files:', filenames)
    # print()
# print(os.environb.get('HOME'))  #to get the home directory.
#Creating a file in home dir. Works in the linux environment. 
# file_path = os.path.join(os.environb.get('HOME'), 'test.txt')
# print(file_path)   #This will create the file properly like /home/sandeep/test.txt 
### How to write to the file that was just created.

# with open(file_path, 'w') as f:
#     f.write 

# print(os.path.basename('/tmp/test.txt'))  #To print the basename 
# print(os.path.split('/tmp/test.txt'))   #This gives both the directory name and basename 

# print(os.path.exists('/tmp/test.txt'))  #To check if the file exists in the path.elif

# # We can also check if it is a directory or file. 


 












