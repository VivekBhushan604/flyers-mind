numbers = [45, 12, 78, 23, 90, 56]

print("Original List:", numbers)

numbers.sort()

print("Sorted List:", numbers)

target = int(input("Enter number to search: "))

if target in numbers:
    print("Number found!")
else:
    print("Number not found!")