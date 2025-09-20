stu_map = {"John": 70, "Alice": 60, "Bob": 85, "Eve": 90, "Charlie": 75}

name = input("Enter the student's name: ")
if name in stu_map:
    print(f"{name}'s score is: {stu_map[name]}")
else:
    print(f"{name} not found in the records.")