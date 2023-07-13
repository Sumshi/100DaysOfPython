	This repo will contain object oriented concepts from freecodecamp
I stopped my 100daysofcode with udemy to focus on 00P this week but will continue it

		RESOURCE USED: javapoint python oop

		PYTHON OBJECTS AND CLASSES:
In conclusion, Python's classes and objects notions are strong ideas that let you write reusable programmes. You may combine information and capabilities into a single entity that is able to be used to build many objects by establishing a class. Using the dot notation, you may access an object's methods and properties after it has been created. You can develop more logical, effective, and manageable code by comprehending Python's classes and objects.


		Python Constructor:
A constructor is a special type of method (function) which is used to initialize the instance members of the class.
Constructors can be of two types.
Parameterized Constructor
Non-parameterized Constructor

In Python, the method the __init__() simulates the constructor of the class. This method is called when the class is instantiated. It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.

Python built-in class functions
The built-in functions defined in the class are described in the following table.

SN	Function	Description
1	getattr(obj,name,default)	It is used to access the attribute of the object.
2	setattr(obj, name,value)	It is used to set a particular value to the specific attribute of an object.
3	delattr(obj, name)	It is used to delete a specific attribute.
4	hasattr(obj, name)	It returns true if the object contains some specific attribute.


Along with the other attributes, a Python class also contains some built-in class attributes which provide information about the class.

The built-in class attributes are given in the below table.

SN	Attribute	Description
1	__dict__	It provides the dictionary containing the information about the class namespace.
2	__doc__	It contains a string which has the class documentation
3	__name__	It is used to access the class name.
4	__module__	It is used to access the module in which, this class is defined.
5	__bases__	It contains a tuple including all base classes.


		Example for setattr:
In the file setattr.py: setattr() sets the attribute name of the person object to the value 'John'. Subsequently, we can access the attribute using dot notation (person.name) and retrieve the value 'John'.
