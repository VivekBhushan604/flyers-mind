import json


class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}\n")


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nStudent {i + 1}")

    student_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, marks)

    students.append({
        "student_id": student.student_id,
        "name": student.name,
        "marks": student.marks
    })


with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nStudents saved successfully.\n")


with open("students.json", "r") as file:
    loaded_students = json.load(file)

print("Students loaded from file:\n")

for student_data in loaded_students:
    student = Student(
        student_data["student_id"],
        student_data["name"],
        student_data["marks"]
    )

    student.display()