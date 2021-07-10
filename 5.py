x = [1, 5, 9, 7]
y = [3, 5, 9, 1]
z = ["a", "d", "f", "r"]

for a, b, c in zip(x, y, z):
    print(a, b, c)

# print(list(zip(x, y, z)))
# print(dict(zip(x, z)))


# For loop temporary variable weirdness
[print(x, y) for x, y in zip(x, y)]
print(x)
# Even though we used x and y as the temporary variables in list
# comprehension to iterate over the zip object, the original x and y are intact.

for x, y in zip(x, y):
    print(x, y)
print(x)
# But if we use x and y as temporary variables in for loop
# the original x and y valures are overwritten.

