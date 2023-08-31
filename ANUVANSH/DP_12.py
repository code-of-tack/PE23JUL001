"""Here is the problem statement for the weekend
You are part of a team developing a scientific calculator called "CalcPro." As part of this calculator, you have been assigned the task of creating a feature that calculates the factorial of a given number. 
This feature will assist users in performing complex mathematical calculations, solving mathematical problems, and analyzing data in various scientific disciplines.
"""

def fact(num):
    """
    Calculates the factorial of a given number.

    Args:
        num (int): The input number.

    Returns:
        int: The factorial value.
    """
    if num == 0 or num ==1:
        return 1
    else:
        return num * fact(num-1)
    
def main():
    """
    Main function to run the CalcPro Factorial Calculation feature.
    """
    print("Welcome to CalcPro Factorial Calculation!")

    number = int(input("Please enter the number for which you want to calculate the factorial: "))

    factorial = fact(number)

    print("\nThank you for providing the number for factorial calculation.")
    print(f"The factorial of {number} is: {factorial}")


if __name__ == '__main__':
    main()