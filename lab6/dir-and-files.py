# Task 1
import os
def list_path(path):
    if os.path.exists(path):
        items = os.listdir(path)
        directories = [item for item in items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]
        for directory in directories:
            print(directory)
        for item in items:
            print(item)
        for file in files:
            print(file)
    else:
        print('Path does not exist.')

# Task 2
def check_path(path):
    if os.path.exists(path):
        print('Path exists!')
        modes = {'Readability': os.R_OK, 'Writability': os.W_OK, 'Executability': os.X_OK}
        for mode, flag in modes.items():
            if os.access(path, flag):
                print(f'{mode}: OK')
            else:
                print(f'{mode}: X')
    else:
        print('Path does not exist.')

# Task 3
def exists_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print(f'Directory: {directory}', f'Filename: {filename}', sep='\n')
    else:
        print('Path does not exist.')

# Task 4
with open('file-for-task-4.txt', 'r') as file:
    line_count = 0
    for x in file:
        if x.strip():
            line_count += 1
    print(line_count)

# Task 5
some_list = ['This', 'is', 'a', 'list']
with open('file-for-task-5.txt', 'a') as file:
    file.write(str(some_list) + '\n')

# Task 6
def increment_letter(letter):
    return chr((ord(letter) - ord('A')) % 26 + ord('A'))
for letter in range(ord('A'), ord('Z') + 1):
    result = increment_letter(chr(letter))
    new_file = open(f'{result}.txt', 'x')

# Task 7
with open('file1-for-task-7.txt', 'r') as file:
    content = file.read()
with open('file2-for-task-7.txt', 'a') as another_file:
    another_file.write(content + '\n')

# Task 8
if os.path.exists('file-for-task-8.txt'):
    os.remove('file-for-task-8.txt')
else:
    print('The file does not exist.')