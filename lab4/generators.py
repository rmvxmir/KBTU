# Task 1
def generate_squares(N):
   for i in range(N):
       yield i ** 2
gen = generate_squares(5)
for i in gen:
    print(i)

# Task 2
def generate_evens(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i
n = int(input("Input a number: "))
even = generate_evens(n)
evens = []
for i in even:
    evens.append(i)
print(*evens, sep=', ')

# Task 3
def generate_spec(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
num = generate_spec(36)
for i in num:
    print(i)

# Task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
square = squares(1, 5)
for i in square:
    print(i)

# Task 5
def generate_back(N):
    for i in range(N, 0, -1):
        yield i
num_back = generate_back(5)
for i in num_back:
    print(i)