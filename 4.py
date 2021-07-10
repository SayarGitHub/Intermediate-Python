test_list = ["left", "right", "top", "bottom"]

[print(i, j) for i, j in enumerate(test_list)]

new_dict = dict(enumerate(test_list))
print(new_dict)
