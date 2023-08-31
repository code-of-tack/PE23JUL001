"""Here is the Problem Statement for Aug 22nd
You are part of a team developing a data analytics platform 
called "DataMetrics." As part of this platform, you have been 
assigned the task of creating a feature that allows users to 
read a CSV (Comma-Separated Values) file and calculate the 
average of a specific column. 
This feature will enable data analysts and business professionals 
to quickly analyze numerical data, gain insights, and make data-driven decisions."""

import os
import csv

def calculate_average(csv_file, column):
    """
    Calculates the average of a specific column in a CSV file.

    Args:
        csv_file (str): The path or name of the CSV file.
        column (str): The name of the column to calculate the average for.

    Returns:
        float: The average value of the specified column.

    """
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        column_values = [float(row[column]) for row in reader]

    #Calculate the average of the column values
    average = sum(column_values) / len(column_values)
    return average

def main():
    """
    Main function to run the DataMetrics data analytics program.
    """
    print("Welcome to DataMetrics Data Analytics!")
    csv_file = input("Please enter the path or name of the CSV file:\n")
    column = input("Please enter the name of the column to calculate the average for:\n")
    
    if not os.path.exists(csv_file):
        print("File not found. Please provide a valid path or name.")
        return

    average = calculate_average(csv_file, column)
    
    if average is None:
        print("There is no data in the specified column")
    else:
        print("Thank you for providing the CSV file.")
        print(f"The average value of the '{column}' column is: ${average}")


if __name__ == "__main__":
    main()