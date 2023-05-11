
### Q1

import math

choice = input("Please enter the area you want to calculate R or r for rectangle, C or c for circle: ").lower()

if choice == 'r':
    width, height = map(float, input("Please enter width and height of the rectangle separated by comma: ").split(','))
    area = width * height
    print(f"The area of a rectangle with width {width} and height {height} is: {area}")

elif choice == 'c':
    radius = float(input("Please enter the radius: "))
    area = math.pi * radius * radius
    print(f"The area of a circle with radius {radius} is {area}")

else:
    print(f"Option {choice} does not exist")

### Q2

student_input = input("Please enter student name and ID separated by space: ")
first_name, last_name, student_id = student_input.split()

if len(student_id) == 7 and student_id.isnumeric() and student_id[0] == '0':
    print(first_name, last_name, student_id)
else:
    print("id must start with 0 and has 7 digits")

### Q3_a

import random

_from, _to = map(int, input("Please enter the range of random numbers from; to: ").split(';'))
rand_num = random.randint(_from, _to - 1)
print(f"The random number between {_from} and {_to} is {rand_num}")
 
### Q3_b

import random

ranges_input = input("Please enter two ranges of random numbers from1;to1 from2;to2 : ")
from1, to1, from2, to2 = map(int, ranges_input.replace(';', ' ').split())

selected_range = random.choice([(from1, to1), (from2, to2)])
rand_num = random.randint(selected_range[0], selected_range[1] - 1)

print(f"The selected range is {selected_range[0]} to {selected_range[1]} and the selected number is {rand_num}")




