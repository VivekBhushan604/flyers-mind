import json


class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print()


students = []

# Number of students
while True:
    try:
        n = int(input("Enter number of students: "))
        if n <= 0:
            print("Number of students must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")


# Student details
for i in range(n):
    print(f"\nStudent {i + 1}")

    while True:
        try:
            student_id = int(input("Enter ID: "))
            break
        except ValueError:
            print("ID must be a number.")

    name = input("Enter Name: ").strip()

    while True:
        try:
            marks = float(input("Enter Marks: "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                continue
            break
        except ValueError:
            print("Marks must be numeric.")

    student = Student(student_id, name, marks)

    students.append({
        "student_id": student.student_id,
        "name": student.name,
        "marks": student.marks
    })


# Save file
try:
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

except Exception as e:
    print("Error while saving:", e)

else:
    print("\nStudents saved successfully.")

finally:
    print("Save operation completed.\n")


# Read file
try:
    with open("students.json", "r") as file:
        loaded_students = json.load(file)

except FileNotFoundError:
    print("students.json not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")

else:
    print("Students loaded from file:\n")

    for student_data in loaded_students:
        student = Student(
            student_data["student_id"],
            student_data["name"],
            student_data["marks"]
        )

        student.display()

finally:
    print("Read operation completed.")