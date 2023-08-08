def calculate_sum_and_average(numbers):
    # Convert the space-separated input string into a list of float numbers
    numbers = [float(i) for i in numbers.split()]

    # Calculate the sum and average of the numbers
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

    return total_sum, average


if __name__ == "__main__":
    print("Welcome to QuantFinTech Data Analytics!")
    numbers_input = input("Please enter a series of numerical data points separated by spaces: ")

    sum_result, average_result = calculate_sum_and_average(numbers_input)
    print("\nThank you for providing the data points.")
    print(f"The sum of the numbers is: {sum_result:.2f}")
    print(f"The average of the numbers is: {average_result:.2f}")