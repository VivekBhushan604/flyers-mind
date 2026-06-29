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


student = Student(101, "Vivek", 89)

student_data = {
    "student_id": student.student_id,
    "name": student.name,
    "marks": student.marks
}

# Save student to JSON
try:
    with open("student.json", "w") as file:
        json.dump(student_data, file, indent=4)

except Exception as e:
    print("Error while saving:", e)

else:
    print("Student saved successfully.")

finally:
    print("Save operation completed.\n")


# Read student from JSON
try:
    with open("student.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    print("student.json not found.")

except json.JSONDecodeError:
    print("Invalid JSON format.")

else:
    loaded_student = Student(
        data["student_id"],
        data["name"],
        data["marks"]
    )

    print("Student loaded successfully:\n")
    loaded_student.display()

finally:
    print("Read operation completed.")