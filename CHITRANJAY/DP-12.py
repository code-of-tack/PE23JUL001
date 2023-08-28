def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():

    print("Welcome to CalcPro Factorial Calculation!")
    try:
        number = int(input("Please enter the number for which you want to calculate the factorial: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
