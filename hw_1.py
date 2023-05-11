Python HW_1


### Q1

name = input("Enter your name: ")
print("Hello " + name + "!")

### Q2

import math

a = float(input("Enter the length of the side of the square: "))

diagonal = math.sqrt(2) * a
area = a * a
perimeter = 4 * a

print("Length of diagonal is:", diagonal)
print("Area is:", area)
print("Circumference is:", perimeter)

### Q3

input_string = input("Enter a string: ")
modified_string = input_string[1:-1]
print(modified_string)

### Q4

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

mid = len(s2) // 2
merged_string = s2[:mid] + s1 + s2[mid:]

print("First string:", s1)
print("Second string:", s2)
print("Merged string:", merged_string)

