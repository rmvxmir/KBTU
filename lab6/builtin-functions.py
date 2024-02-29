# Task 1
def list_multiplication(some_list):
    res = 1
    for i in range(len(some_list)):
        res *= some_list[i]
    return res

print(list_multiplication([1, 2, 3])) # Outputs '6'

# Task 2
def count_upper_lower(string):
    upper_count = lower_count = 0
    for i in range(len(string)):
        if string[i].isupper():
            upper_count += 1
        elif string[i].islower():
            lower_count += 1
    return upper_count, lower_count

print(count_upper_lower("AaBbCcDd")) # Outputs '(4, 4)'

# Task 3
def palindrome_check(string):
    reversed_string = ''.join(reversed(string))
    if string == reversed_string:
        return True
    else:
        return False

print(palindrome_check('abvvba')) # Outputs 'True'
print(palindrome_check('nopalindrome')) # Outputs 'False'

# Task 4
from time import sleep
def square_root(num, ms):
    sleep(ms / 1000.0)
    print(f"Square root of {num} after {ms} milliseconds is: {pow(num, 0.5)}")

square_root(25100, 2123) # Outputs "Square root of 25100 after 2123 miliseconds is 158.42979517754858"

# Task 5
def true_elements(some_tuple):
    return all(some_tuple)

print(true_elements((True, True))) # Outputs 'True'
print(true_elements((True, False))) # Outputs 'False'