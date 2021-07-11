# How to create our own generators


def simple_gen():
    yield "Oh"
    yield "Hello"
    yield "There"


[print(i) for i in simple_gen()]

CORRECT_COMBO = (3, 4, 6)


# Okay level implementation
found = False
for c1 in range(10):
    if found:
        break
    for c2 in range(10):
        if found:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print("Found the correct combination:{}".format((c1, c2, c3)))
                found = True
                break

# Good implementation
for i in range(100, 1000):
    if (i // 100, (i % 100) // 10, (i % 100) % 10) == CORRECT_COMBO:
        print(
            "Found the correct combination:{}".format(
                (i // 100, (i % 100) // 10, (i % 100) % 10)
            )
        )
        break

# Fancy implementation
def code_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                if (c1, c2, c3) == CORRECT_COMBO:
                    yield (c1, c2, c3)


for c1, c2, c3 in code_gen():
    if (c1, c2, c3) == CORRECT_COMBO:
        print("Found the correct combination:{}".format((c1, c2, c3)))
        break

