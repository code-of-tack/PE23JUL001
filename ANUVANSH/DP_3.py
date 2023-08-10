"""
Here is the Problem Statement for Aug 9th
You are part of a team developing a financial planning application called "FinPlanPro." 
As part of this application, you have been assigned the task of creating a feature that generates the Fibonacci sequence up to a given number 'n'. 
This feature will assist financial planners and investment advisors in performing calculations related to interest rates, asset growth, and investment strategies.
"""

def generate_fibonacci(n):
    """
       Generates the fibonacci sequence upto n.
     
       Args:
            n (int): the number upto which fib sequence is to be generated

       Returns:
            list: list of fib sequence upto n

       """
    a, b = 0, 1
    fibonacci_sequence = []
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def main():
    """
    Main function to run the FinPlanPro Fibonacci Generator.
    
    """
    
    print("Welcome to FinPlanPro Fibonacci Generator!")
    n = int(input("Please enter the desired number n to generate the Fibonacci sequence:\n"))
    
    fibonacci_result = generate_fibonacci(n)
    fibonacci_string = ', '.join(map(str, fibonacci_result))  #create a single string that represents the Fibonacci sequence in a formatted manner i.e puts ', '
    
    print("\nThank you for providing the number 'n'.")
    print(f"The Fibonacci sequence up to {n} is: {fibonacci_string}")

if __name__ == '__main__':
    main()
