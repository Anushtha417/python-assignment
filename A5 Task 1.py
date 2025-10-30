# Step 1: Create dictionary of student marks
student_marks = {
    "Anushtha": 92,
    "Rahul": 85,
    "Priya": 88,
    "Aman": 79,
    "Sneha": 95
}

# Step 2: Ask user for student name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks or show not found message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")
