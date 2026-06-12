num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    exit()

if num % 2 == 0:
    print("Even")
else:
    print("Odd")