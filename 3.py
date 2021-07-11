# range() is a generator. List comprehension saves entire list to memory. So,
# generally list comprehensions are memory heavy but fast to iterate over.
# Whereas generators are more memory efficient, but slow to iterate over.


x = [i for i in range(5)]  # list comprehension
print("a", x)
y = (i for i in range(5))  # generator expression
print("b", y)

for i in y:
    print("c", i)


def div_five(num):
    return num % 5 == 0


input_list = [1, 5, 10, 15, 20, 7, 9, 3, 9]
result = (i for i in input_list if div_five(i))
print("d", result)
[print("e", i) for i in result]  # basically acts as one-line for loop here

result = [i for i in input_list if div_five(i)]
print("f", result)
[print("g", i) for i in result]

[
    [print(i, ii) for ii in range(5)] for i in range(5)
]  # nested loops usinng list comprehension

