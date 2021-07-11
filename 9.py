# The general syntax of a lambda function is quite simple:

# lambda argument_list: expression

# The argument list consists of a comma separated list of arguments and the
# expression is an arithmetic expression using these arguments. You can assign
# the function to a variable to give it a name.

# The following example of a lambda function returns the sum of its two
# arguments:

sum = lambda x, y: x + y
print(sum(3, 4))

# -----------------------------------------------------------------------------#

# The advantage of the lambda operator can be seen when it is used in
# combination with the map() function. map() is a function which takes two
# arguments:

# r = map(func, seq)

# The first argument func is the name of a function and the second a sequence
# (e.g. a list) seq. map() applies the function func to all the elements of the
# sequence seq. Before Python3, map() used to return a list, where each element
# of the result list was the result of the function func applied on the
# corresponding element of the list or tuple "seq". With Python 3, map() returns
# an iterator. The following example illustrates the way of working of map():


def fahrenheit(T):
    return (float(9) / 5) * T + 32


def celsius(T):
    return (float(5) / 9) * (T - 32)


# The iterator returned by map function can only be used/iterated once once
temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheit, temperatures))
C = list(map(celsius, F))
print(F)
print(C)

# In the example above we haven't used lambda. By using lambda, we wouldn't have
# had to define and name the functions fahrenheit() and celsius().

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9) / 5) * x + 32, C))
C = list(map(lambda x: (float(5) / 9) * (x - 32), F))
print(F)
print(C)

# map() can be applied to more than one list. The lists don't have to have the
# same length. map() will apply its lambda function to the elements of the
# argument lists, i.e. it first applies to the elements with the 0th index, then
# to the elements with the 1st index until the n-th index is reached:

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))

# If one list has fewer elements than the others, map will stop when the shortest
# list has been consumed:

a = [1, 2, 3]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

print(list(map(lambda x, y, z: 2.5 * x + 2 * y - z, a, b, c)))

# -----------------------------------------------------------------------------#

# The function filter(f,l) needs a function f as its first argument. f has to
# return a Boolean value, i.e. either True or False. This function will be
# applied to every element of the list l. Only if f returns True will the element
# be produced by the iterator, which is the return value of filter(function,
# sequence).

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)


# -----------------------------------------------------------------------------#

# The function

# reduce(func, seq)

# continually applies the function func() to the sequence seq. It returns a
# single value.

# If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:

# At first the first two elements of seq will be applied to func, i.e.
# func(s1,s2) The list on which reduce() works looks now like this: [ func(s1,
# s2), s3, ... , sn ] In the next step func will be applied on the previous
# result and the third element of the list, i.e. func(func(s1, s2),s3) The list
# looks like this now: [ func(func(s1, s2),s3), ... , sn ] Continues like this
# until just one element is left and returns this element as the result of
# reduce()


import functools

print(functools.reduce(lambda x, y: x + y, [47, 11, 42, 13]))

