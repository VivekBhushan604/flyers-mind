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


student = Student(101, "Vivek", 89)

print("\nStudent object details:")
student.display()

student_data = {
    "student_id": student.student_id,
    "name": student.name,
    "marks": student.marks
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("\nStudent saved in student.json.\n")

with open("student.json", "r") as file:
    data = json.load(file)

loaded_student = Student(
    data["student_id"],
    data["name"],
    data["marks"]
)

print("Student loaded from file:")
loaded_student.display()