import subprocess

subprocess.run('dir', shell=True)   #Runs the command.
#if you dont want to use the shell as True then pass the argument as the list

subprocess.run(['ls', '-al'])   #Run the arguments as the list
#Standard out goes to the output in the editor

p1 = subprocess.run(['ls', '-al'])
print(p1)  #Completed process.
print(p1.args) #Prints all the arguments that are passed.ArithmeticError
print(p1.returncode)   #0 for the successful
print(p1.stdout)  #Result would be None -- Sendind the standard out to console

p2 = subprocess.run(['ls' , '-al'], capture_output= True) #This will output to the p2 variable and need to run stdout to see the result.

print(p2.stdout)   #This will output to bytes.

print(p2.stdout.decode())  #To give better output by converting to string.

p3 = subprocess.run(['ls', '-al'], capture_output=True, text=True) #Instead of converting to the string.
print(p3.stdout)

#Redirecting the stdout to a pipe

p4 = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE, text=True)
print(p4.stdout)

#Lets direct it to a file insted of somewhere

with open('output.txt', 'w') as f:
    p5 = subprocess.run(['ls', '-al'], stdout=f, text=True)


#List the contents of a dir that doesnt exist:
p6 = subprocess.run(['ls', '-al', 'folder'], capture_output = True, text=True, check=True)
print(p6.stderr)

#Redirect the error to Null

p7 = subprocess.run(['ls', '-al', 'folder'], stderr = subprocess.DEVNULL)
print(p7.stderr)



