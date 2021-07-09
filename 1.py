names = ["James", "owen", "Chimi", "Klei"]
print(', '.join(names))

import os
location = "C:\\Users\\Sayar\\Tutorials\\Intermediate-Python"
file_name = "example.txt"

with open(os.path.join(location, file_name)) as f:
    print(f.read()) 