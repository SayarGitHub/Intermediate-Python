# In Python, functions are first-class objects. This means that functions can be
# passed around and used as arguments, just like any other object (string, int,
# float, list, and so on). Consider the following three functions:


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


# Note that greet_bob(say_hello) refers to two functions, but in different ways:
# greet_bob() and say_hello. The say_hello function is named without parentheses.
# This means that only a reference to the function is passed. The function is not
# executed. The greet_bob() function, on the other hand, is written with
# parentheses, so it will be called as usual.


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))
print(greet_bob(be_awesome))

# It’s possible to define functions inside other functions. Such functions are
# called inner functions. Here’s an example of a function with two inner
# functions:


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()

# Furthermore, the inner functions are not defined until the parent function is
# called. They are locally scoped to parent(): they only exist inside the
# parent() function as local variables. Try calling first_child().

# Python also allows you to use functions as return values. The following example
# returns one of the inner functions from the outer parent() function:


def parent_1(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


# Note that you are returning first_child without the parentheses. Recall that
# this means that you are returning a reference to the function first_child. In
# contrast first_child() with parentheses refers to the result of evaluating the
# function.

print(parent_1(1))

first = parent_1(1)
second = parent_1(2)

# You can now use first and second as if they are regular functions, even though
# the functions they point to can’t be accessed directly:

print(first())
print(second())

# Decorators


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)  # decoration

say_whee()

# In effect, the name say_whee now points to the wrapper() inner function.
# Remember that you return wrapper as a function when you call
# my_decorator(say_whee). Put simply: decorators wrap a function, modifying its
# behavior.

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee_1():
    print("Whee!")


say_whee_1 = not_during_the_night(say_whee_1)

say_whee_1()


@my_decorator
def say_whee_2():
    print("Whee!")


say_whee_2()

# So, @my_decorator is just an easier way of saying say_whee =
# my_decorator(say_whee)

from do_twice import do_twice


@do_twice
def say_whee_3():
    print("Whee!")


say_whee_3()

# Decorating Functions With Arguments
@do_twice
def greet(name):
    print(f"Hello {name}")


greet("World")

# Returning Values From Decorated Functions
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


print(
    return_greeting("Sayar")
)  # this gives None if the wrapper function does not return the evaluated value


# Introspection

