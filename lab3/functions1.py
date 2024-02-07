# Task 1
def ounces_to_grams(grams):
    ounces = 28.3495231 * grams
    return ounces
    
# Task 2
def convert(F):
    C = (5 / 9) * (F - 32)
    return C

# Task 3
def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        total_legs = 2 * numchickens + 4 * numrabbits
        
        if total_legs == numlegs:
            return numchickens, numrabbits
        
    return None

# Task 4
def isPrime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True
        
def filter_prime(num_list):
    for i in num_list:
        if isPrime(i):
            print(i, end = ' ')

# Task 5
from itertools import permutations
def print_permutations(string):
    permuted_strings = permutations(string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))


# Task 6
def reversed_string(somestr):
    slist = somestr.split()
    slist = slist[::-1]
    print(*slist)

# Task 7
def has_33(nums):
    for i in range(0, len(nums) + 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8
def spy_game(nums):
    order = 0
    for i in nums:
        if i == 0 and order < 2:
            order += 1
        elif i == 7 and order == 2:
            return True
    return False

# Task 9
def volume(r):
    V = (4 / 3) * 3,14 * (r ** 3)
    return V

# Task 10
def unique(num_list):
    uni_list = []
    for i in num_list:
        if i not in uni_list:
            uni_list.append(i)
    print(*uni_list)

# Task 11
def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

# Task 12
def histogram(*args):
    for i in args[0]:
        for k in range(0, i):
            print('*', end = '')
        print()

# Task 13
# guessgame.py