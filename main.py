from operation import *



memory = None     # for M+ feature


def show_menu():
    print("\n------ Scientific Calculator ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    print("5. Square")
    print("6. Cube")
    print("7. Power (x^y)")

    print("8. Square Root")
    print("9. Cube Root")

    print("10. Sin")
    print("11. Cos")
    print("12. Tan")

    print("13. Asin")
    print("14. Acos")
    print("15. Atan")

    print("16. Log base 10")
    print("17. Natural log (ln)")
    print("18. Antilog")

    print("19. Store last result in memory (M+)")
    print("20. Use memory value")

    print("0. Exit")


def get_number(msg):
    return float(input(msg))


last_result = None

while True:
    show_menu()
    choice = input("Enter your choice: ")



    if choice == "1":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        last_result = add(a, b)
        print(last_result)

    elif choice == "2":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        last_result = sub(a, b)
        print(last_result)

    elif choice == "3":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        last_result = mul(a, b)
        print(last_result)

    elif choice == "4":
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        last_result = div(a, b)
        print(last_result)

    elif choice == "5":
        x = get_number("Enter number: ")
        last_result = square(x)
        print(last_result)

    elif choice == "6":
        x = get_number("Enter number: ")
        last_result = cube(x)
        print(last_result)

    elif choice == "7":
        x = get_number("Enter base: ")
        y = get_number("Enter power: ")
        last_result = power(x, y)
        print(last_result)

    elif choice == "8":
        x = get_number("Enter number: ")
        last_result = square_root(x)
        print(last_result)

    elif choice == "9":
        x = get_number("Enter number: ")
        last_result = cube_root(x)
        print(last_result)

    elif choice == "10":
        x = get_number("Enter angle in degrees: ")
        last_result = sin(x)
        print(last_result)

    elif choice == "11":
        x = get_number("Enter angle in degrees: ")
        last_result = cos(x)
        print(last_result)

    elif choice == "12":
        x = get_number("Enter angle in degrees: ")
        last_result = tan(x)
        print(last_result)

    elif choice == "13":
        x = get_number("Enter value (-1 to 1): ")
        last_result = asin(x)
        print(last_result)

    elif choice == "14":
        x = get_number("Enter value (-1 to 1): ")
        last_result = acos(x)
        print(last_result)

    elif choice == "15":
        x = get_number("Enter value: ")
        last_result = atan(x)
        print(last_result)

    elif choice == "16":
        x = get_number("Enter number: ")
        last_result = log10(x)
        print(last_result)

    elif choice == "17":
        x = get_number("Enter number: ")
        last_result = ln(x)
        print(last_result)

    elif choice == "18":
        x = get_number("Enter number: ")
        last_result = antilog(x)
        print(last_result)

    # -------- Memory Feature --------
    elif choice == "19":
        if last_result is None:
            print("No result to store.")
        else:
            memory = last_result
            print("Stored in memory.")

        continue

    elif choice == "20":
        if memory is None:
            print("Memory is empty.")
        else:
            print("Memory value:", memory)
        continue

    elif choice == "0":
        print("Calculator closed.")
        break

    else:
        print("Invalid choice.")
        continue

    print("Result =", last_result)


