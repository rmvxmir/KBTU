# Task 1
class upperString():
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("")

    def printString(self):
        print(self.input_string.upper())

some_string = upperString() # Test output
some_string.getString()
some_string.printString()

# Task 2
class Shape():
    def __init__(self):
        pass
    def area(self):
        print('0')

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def get_area(self):
        print(self.length ** 2)

square = Square(12) # Test output
square.get_area()

# Task 3
class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
    
    def compute_area(self):
        print(self.length * self.width)

some_rectangle = Rectangle(10, 12) # Test output
some_rectangle.compute_area()

# Task 4
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    
    def move(self, nx, ny):
        self.x += nx
        self.y += ny
        print(f"New coordinates: ({self.x}, {self.y})")

    def dist(self, other_point):
        print("Distance between 2 points: ", math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2))

point = Point(1, 2) # Test output
point.show()
point.move(3, 4)
second_point = Point(4, 7)
point.dist(second_point)

# Task 5
class Account():
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print(f"Withdrawal not allowed. Balance: ${self.balance}")

account = Account(owner="Amir R", balance=1000.0) # Test output
account.deposit(500.0)
account.withdraw(1000.0)
account.withdraw(501.0)

# Task 6
def isPrime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Test output
prime_numbers = list(filter(lambda x: isPrime(x), numbers))
print("Prime numbers:", prime_numbers)
