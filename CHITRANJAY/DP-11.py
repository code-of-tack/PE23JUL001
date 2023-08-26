"""
You are part of a team developing a data analytics platform called "DataMetrics."
As part of this platform, you have been assigned the task of creating a feature that allows users to
read a CSV (Comma-Separated Values) file and calculate the average of a specific column.
This feature will enable data analysts and business professionals to quickly analyze
numerical data, gain insights, and make data-driven decisions.
To accomplish this, you decide to create a program that reads a CSV file and
calculates the average of a specific column. The program will provide users with
the average value, along with additional functionality to enhance their data analysis capabilities.
"""


import csv


def calculate_average(csv_file, column_name):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            column_data = []

            for row in reader:
                column_data.append(float(row[column_name]))

            if column_data:
                average = sum(column_data) / len(column_data)
                return average
            else:
                return None
    except FileNotFoundError:
        return None


def main():
    print("Welcome to DataMetrics Data Analytics!")
    csv_file = input("Please enter the path or name of the CSV file: ")
    column_name = input("Please enter the name of the column to calculate average for: ")

    average = calculate_average(csv_file, column_name)

    if average is not None:
        print(f"The average value of the '{column_name}' column is: {average:.2f}")
    else:
        print("An error occurred. Please check the CSV file and column name.")


if __name__ == "__main__":
    main()
