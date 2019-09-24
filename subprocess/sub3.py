#This program takes the output of one command and uses that as input of other

import subprocess

p1 = subprocess.run(['cat', 'sample.txt'], capture_output= True, text=True)
#print(p1.stdout)

p2 = subprocess.run(['grep', '-n', 'test'], capture_output=True, text=True, input=p1.stdout)
print(p2.stdout)

#Another method for the sameoutput, here we use the shell=True which doesnt need to give the arguments as the lists.

p3 = subprocess.run('cat sample.txt | grep -n test', capture_output=True, text=True, shell=True)
print(p3.stdout)

