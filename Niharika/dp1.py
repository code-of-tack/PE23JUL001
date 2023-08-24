def calculate_sum(numbers):
    """
    Calculates the sum of a series of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The sum of the numbers.
    """
    return sum(numbers)
  

def calculate_average(numbers):
    """
    Calculates the average of a series of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)
def main():
    """
    Main function to run the data analytics program.
    """
    print("Welcome to QuantFinTech Data Analytics!")
    data_points = input("Please enter a series of numerical data points separated by spaces:\n")

    # Convert the input string into a list of numbers
    numbers = [float(num) for num in data_points.split()]

    # Calculate the sum and average
    total_sum = calculate_sum(numbers)
    average = calculate_average(numbers)

    print("\nThank you for providing the data points.")
    print("The sum of the numbers is:", total_sum)
    print("The average of the numbers is:", average)


# Run the program
if __name__ == '__main__':
    main()