def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence

def main():
    print("Welcome to FinPlanPro Fibonacci Generator!")
    n = int(input("Please enter the desired number 'n' to generate the Fibonacci sequence: "))
    
    fibonacci_sequence = generate_fibonacci(n)
    
    print(f"Thank you for providing the number '{n}'.")
    print(f"The Fibonacci sequence up to {n} is: {', '.join(map(str, fibonacci_sequence))}")

if __name__ == "__main__":
    main()