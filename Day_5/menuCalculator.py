while True:
    print("\n===== Calculator Menu =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting calculator.")
        break

    elif choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print("Result =", a + b)

        elif choice == "2":
            print("Result =", a - b)

        elif choice == "3":
            print("Result =", a * b)

        elif choice == "4":
            if b == 0:
                print("Division by zero is not allowed.")
            else:
                print("Result =", a / b)

    else:
        print("Invalid choice.")