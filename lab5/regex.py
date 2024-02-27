import re

with open('row.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Task 1
pattern = re.compile(r'ab*')
matches = re.findall(pattern, content)
for match in matches:
    print(match)

# Task 2
pattern = re.compile(r'ab{2, 3}')
matches = re.findall(pattern, content)
for match in matches:
    print(match)

# Task 3
pattern = re.compile(r'[a-z]+_[a-z]+')
matches = re.findall(pattern, content)
for match in matches:
    print(match)

# Task 4
pattern = re.compile(r'[A-Z]{1}[a-z]+')
matches = re.findall(pattern, content)
for match in matches:
    print(match)

# Task 5
pattern = re.compile(r'a.*b$')
matches = re.findall(pattern, content)
for match in matches:
    print(match)

# Task 6
pattern = r'[ ,.]'
upd = re.sub(pattern, ':', content)
print(upd)

# Task 7
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)
print(snake_to_camel(content))

# Task 8
pattern = r'[A-Z]'
upd = re.split(pattern, content)
print(upd)

# Task 9
pattern = r'([a-z])([A-Z])'
upd = re.sub(pattern, r'\1 \2', content)
print(upd)

# Task 10
camelCase = "ThisIsCamelCase"
snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', camelCase)
print(snake_case.lower())