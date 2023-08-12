'''
You are part of a team developing a financial planning application called "FinPlanPro." 
As part of this application, you have been assigned the task of creating a feature that
generates the Fibonacci sequence up to a given number 'n'. This feature will assist 
financial planners and investment advisors in performing calculations related to interest 
rates, asset growth, and investment strategies.

'''
def generate_fibonacci_sequence(n):
 
 

 '''
  Generates Fibonacii sequence

  Args: 
     n:Number of fibonacci sequence
  Returns:
     fib_sequence:List of numbers in Fibonacci sequence
     

 '''
 
 fib_sequence=[0,1]
 

 while True:
  next_num=fib_sequence[-1]+fib_sequence[-2]
  
  if(next_num<=n):
    fib_sequence.append(next_num)
  else:
     break 
 return fib_sequence


def main():
  '''
  Main Function to run FinPlanPro Fibonacii Generator
  '''
  print("Welcome to FinPlanPro Fibonacci Generator!")
  n = int(input("Please enter the desired number 'n' to generate the Fibonacci sequence: "))
    
  fib_sequence = generate_fibonacci_sequence(n)
    
  print(f"Thank you for providing the number 'n': {n}.")
  print(f"The Fibonacci sequence up to {n} is: {', '.join(map(str, fib_sequence))}")

if __name__ == "__main__":
    main()
