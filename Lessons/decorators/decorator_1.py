"""Putting a Wrapper Around a Function.

Metaprogramming is about creating functions and classes whose main
goal is to manipulate code. The main features of this include
decorators. Class decorators and meta classes.

A decorator is a function that accepts a function as input and returns
a new function as output.

Decorator are used to modify the behavior of function or class.

Syntax of Decorator
-------------------

@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)'''

"""


# Defining a decorator
def hello_decorator(func):
    """Define a decorator."""

    def inner_1():
        """Wrap function.

        Wrapper function which argument is called
        """
        print("This is before function execution")
        func()
        print("This is after function execution")

    return inner_1


# Defining a function to be called inside the wrapper
def func_to_be_used():
    """Function to be called inside wrapper."""
    print("This is inside the function!!")


# # Example use
func_to_be_used = hello_decorator(func_to_be_used)
func_to_be_used()
