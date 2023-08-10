"""
You are part of a team developing a financial planning application called "FinPlanPro."
As part of this application, you have been assigned the task of creating a feature that generates
the Fibonacci sequence up to a given number 'n'.
This feature will assist financial planners and investment advisors in performing calculations related to
interest rates, asset growth, and investment strategies.
To accomplish this, you decide to create a program that generates the Fibonacci sequence up to a given number 'n'.
The program will provide users with the Fibonacci sequence,
along with additional functionality to enhance their financial planning capabilities.
"""
def generate_fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to a given number 'n'.
        List[int]: The Fibonacci sequence up to the given number 'n'.
    """
    sequence = [0, 1]  # Initialize the sequence with the first two numbers

    while sequence[-1] + sequence[-2] <= n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

def main():
    """
    Main function to run the FinPlanPro Fibonacci Generator.
    """
    print("Welcome to FinPlanPro Fibonacci Generator!")

    n = int(input("Please enter the desired number 'n' to generate the Fibonacci sequence: "))

    fibonacci_sequence = generate_fibonacci_sequence(n)
    print("\nThank you for providing the number 'n'.")
    print("The Fibonacci sequence up to", n, "is:", ', '.join(map(str, fibonacci_sequence)))

if __name__ == '__main__':
    main()