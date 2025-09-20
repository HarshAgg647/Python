file = ".\TuteDude\Assignment 4\sample.txt"

try:
    with open(file, 'r') as f:
        content = f.readlines()
        for line in content:
            print(line.strip())
except FileNotFoundError:
    print(f"The file {file} does not exist.")
    
    