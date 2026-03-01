def calculator():
    history = []

    while True:
        print("""
=============================
      PYTHON CALCULATOR
=============================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Modulus
7. Show History
8. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "8":
            print("Thanks for using Calculator!")
            break

        # Show history
        if choice == "7":
            if len(history) == 0:
                print("No history available.")
            else:
                for item in history:
                    print(item)
            continue

        try:
            numbers = list(map(float,
                               input("Enter numbers separated by space: ").split()))

            if len(numbers) == 0:
                print("Enter numbers!")
                continue

        except ValueError:
            print("Invalid input!")
            continue

        result = None

        if choice == "1":
            result = sum(numbers)
            operation = " + ".join(map(str, numbers))

        elif choice == "2":
            result = numbers[0]
            operation = str(numbers[0])
            for num in numbers[1:]:
                result -= num
                operation += f" - {num}"

        elif choice == "3":
            result = 1
            operation = " * ".join(map(str, numbers))
            for num in numbers:
                result *= num

        elif choice == "4":
            try:
                result = numbers[0]
                operation = str(numbers[0])
                for num in numbers[1:]:
                    result /= num
                    operation += f" / {num}"
            except ZeroDivisionError:
                print("Division by zero error!")
                continue

        elif choice == "5":
            result = numbers[0]
            operation = " ** ".join(map(str, numbers[1:]))
            for num in numbers[1:]:
                result **= num

        elif choice == "6":
            result = numbers[0]
            operation = " % ".join(map(str, numbers[1:]))
            for num in numbers[1:]:
                result %= num

        else:
            print("Invalid choice!")
            continue

        print("Result =", result)

        # Store history
        history.append(f"{operation} = {result}")


calculator()