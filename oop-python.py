#!/usr/bin/python -tt

### OOP Demonstration in Python

## Introduction
## http://www.voidspace.org.uk/python/articles/OOP.shtml

## Creating New Objects

# Python's datatypes have their own 'blueprint'
# the integer (int), the float (float), booleans (bool),
# lists (list), dictionaries (dict), and more.

# For these built in datatypes, we can either use normal
# Python syntax to create them - or we can use the blueprint itself (the type).

print (' ')
print 'Creating New Objects'
print (' ')

# create a dictionary the normal way
a_dict = {
    'key' : 'value',
    'key2' : 'value2'
    }

# use 'dict' to create one
list_of_tuples = [('key', 'value'),
                 ('key2', 'value2')]

a_dict_2 = dict(list_of_tuples)

# Should print True
print a_dict == a_dict_2

# Should print <type 'dict'>
print type(a_dict)


# Should print <type 'dict'>
print type(a_dict_2)


a_dict = {
    'key' : 'value',
    'key2' : 'value2'
    }

a_dict_2 = a_dict.copy()

# Should print True
print a_dict == a_dict_2

a_dict.clear()

# Should print {}
print a_dict

# Should print <built-in method clear of dict object at 0x0012E540>
print a_dict.clear

# Should print <type 'builtin_function_or_method'
print type(a_dict.clear)

print(' ')
print('---------------------')
print(' ')

## Functions are Objects

print 'Functions are Objects'
print (' ')

# Have you ever written code that looks a bit like this ?

# if value == 'one':
#     # do something
#     function1()
# elif value == 'two':
#     # do something else
#     function2()
# elif value == 'three':
#     # do something else
#     function3()
# Other languages have a construct called switch that makes writing code
# like that a bit easier.

# In Python we can achieve the same thing (in less lines of code) using a
# dictionary of functions.

def function1():
    print 'You chose one.'
def  function2():
    print 'You chose two.'
def  function3():
    print 'You chose three.'


# switch is our dictionary of functions
switch = {
    'one': function1,
    'two': function2,
    'three': function3,
    }

# choice can eithe be 'one', 'two', or 'three'
choice = raw_input('Enter one, two, or three :')

# call one of the functions
try:
    result = switch[choice]
except KeyError:
	print 'I didn\'t understand your choice.'
else:
    result()

print(' ')
print('---------------------')
print(' ')


## User Defined Classes

print 'User Defined Classes'
print (' ')

class OurClass(object):
    """Class docstring."""

    # defines the initialization of the OurClass object
    # requires three args
    # self is taken directly
    # self.arg1 is similar to this.arg1 in Java
    def __init__(self, arg1, arg2):
        """Method docstring."""
        self.arg1 = arg1
        self.arg2 = arg2

    def printargs(self):
        """Method docstring."""
        print self.arg1
        print self.arg2

# an instance of the class OurClass is created
instance = OurClass('arg1', 'arg2')

# Should print <class 'OurClass'>
print type(instance)

# Should print arg1 arg2
instance.printargs()


print(' ')
print('---------------------')
print(' ')
