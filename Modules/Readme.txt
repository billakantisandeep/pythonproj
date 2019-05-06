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
