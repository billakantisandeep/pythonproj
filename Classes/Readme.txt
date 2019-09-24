#This file is corresponding to the Readme of classes in python.
Classes: Python object oriented programming
- Logically group the data and functions to reuse and build upon.
- Attributes and methods. -- Data and functions.


  Class -- Blue print and create instances for the class

  Inhertiance Mechanism -- allows multiple base classes.

  First look at the class
  class classname:
  <stat1>
  .
  .
  .
  .
  .
  <stat2>

  Statments inside the class would be the function definitions.
  function definitions inside the class will be peculiar form of argument list, dictated by the calling conventions for methods.

  class objects: attribute references and instantiation.
  Attribute references  ex: Myclass.i and Myclass.f
  instantiation:   x = Myclass()  #Creates new instance of the class and assigns the object to local variable x
  Special method __init__
  def __init__
      self.data =[]

Instance Objects:
Attribute references.
two kinds of valid attribute names -- data attributes and methods.





----------------------

Class variables : Shared across all the instances of the class.
Instance variables will be unique :   -- Name, email and pay.
Class variables should be same for all instances.

Class or static variables are shared by all objects. ...
The Python approach is simple, it doesn't require a static keyword.
All variables which are assigned a value in class declaration are class variables.
And variables which are assigned values inside class methods are instance variables.

Class variables can be called from class i.e Employee.raise_amount or self.raise_amount -- self.raise_amount will give you chance to change any only instance.


class methods vs static methods.

Regualar methods -- automatically calls first argument as self. -- automatically takes instance as the first method like self.
Class methods --- automcatically calls first arguments as cls
Static methods -- empty

Instance methods Vs class methods vs static methods.
Decorater pattern or simple call decorater.
Decoraters are simple functions  -- they apply logic or change the behaviour of other functions.
They are an excellent way to reuse code, and can help to separate logic into individual concerns.

Instance Methods: The most common method type. Able to access data and properties unique to each instance.
Static Methods: Cannot access anything else in the class. Totally self-contained code.
Class Methods: Can access limited methods in the class. Can modify class specific details.








