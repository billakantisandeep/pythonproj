Modele contains both executable statements and function definitions. 
- Executable statements are intented to initialize the module and executed only the first time the module name is encountered in an import statement.
- Each module has its own private symbol table, which is used as the global symbol table by all the functions defined in the module. 
modname.itemname -- refer to its functions. 

Module search path : First interpreter searches for built-in modules if it is not found there then it goes for the sys.path -- Current dir, Python path, installation-dependent. 
Complied python files -- To speed up uploading modules, python caches the compiled version of each module in __pycache__ dir under the name module.version.pyc 


-> dir()  : Used to find out which names a moduele defines. It lists all variables, functions, modules etc..

For builtin functions and variables: 
import builtins
dir(builtins)

Packages: Packages are a way of structuring python module namespaces by using dotted module names. 
a.b -- submodule b in the package all
__init__.py -- files are required to make python treat directories containing the file as packages. __init__.py can be a empty file.

----------------------------------------------------------------------------

#Import a module with different name
import module_name as mod ( For importing in shortcut)

#Import function in the module instead of whole module
from module_name import function (this imports what exactly we need)


#Import more than one function
from module_name import function, test ( To import function and test variable)

#Import everything
from module_name import *   ( It imports all the ones and this is not better approach as it makes hard to track down.)

Module path -->  sys.path -> 1.Directory local where script runs, 2. Python path env variable --> Standard lib Directory --> Site packages dir(third party)

#Adding a new folder to sys path for programs to check the modules in folder.
sys.path.append('/home/sandeep/Desktop/My_module')   #Not the best approach.

#Better approach will be adding to PythonPATH Environmental variables.
-> Linux  .bashrc -> export PYTHONPATH = /home/sandeep/Desktop/My_module
-> Windows -> Start -> Computer -> Properties -> Advanced settings -> Evn variables -> PYTHONPATH = C:\Users\sandeep\Desktop\My_module

Standard Library : Already that functionality is already written by best programmers and we can use them.

--------------------------
What does import . from