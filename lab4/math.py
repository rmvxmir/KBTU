import math
# Task 1
degree = int(input("Input degree: "))
print("Output radian:", math.radians(degree))

# Task 2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Area:", (a + b) / 2 * h)

# Task 3
side_num = int(input("Input number of sides: "))
side_len = float(input("Input the length of a side: "))
print("The area of the polygon is:", int((1/4) * side_num * side_len**2 / math.tan(math.pi / side_num)))

# Task 4
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
print("Area:", base * height)