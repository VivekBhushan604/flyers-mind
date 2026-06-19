marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1} out of 100: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\nMarks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)