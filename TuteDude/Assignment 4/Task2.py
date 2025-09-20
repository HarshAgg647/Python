file = "./TuteDude/Assignment 4/output.txt"

with open(file, 'w') as f:
    message = input("Enter a message to write to the file: ")
    f.write(message)
    print(f"Message written to output.txt")
    
with open(file, 'a') as f:
    additional_message = input("Enter an additional message to append to the file: ")
    f.write("\n" + additional_message)
    print(f"Additional message appended to output.txt")
    
with open(file, 'r') as f:
    print("Final Content of output.txt:")
    content = f.readlines()
    for line in content:
        print(line.strip())
    