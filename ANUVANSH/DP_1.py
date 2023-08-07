"""Problem Statement for August 7th(DP-1)
You are part of a team developing an advanced financial analytics platform for a 
leading investment firm called "QuantFinTech." As part of this platform, you have been assigned 
the task of creating a feature that allows investment analysts to quickly calculate the sum and average 
of a series of numerical data points. This feature will assist analysts in assessing the performance of 
investment portfolios, evaluating risk factors, and making informed investment decisions.
"""

def sum_average(nums):
    """Calculates the sum and average of a series of numerical data points.
    
       Args:
            nums (list of floats): The series of numbers for which we have to calculate sum and average.
       
       Returns:
            tuple: The sum(i.e tuple[0]) and average(i.e tuple[1]) of the series
    """
    total = 0

    for k in range(0, len(nums)):
        total = total + nums[k]

    return total, total/len(nums)


def main():
    """This is the main function to run the QuantFinTech - Sum 
    and Average feature."""

    print("Welcome to QuantFinTech Data Analytics!")
    
    num_data_points = input("Please enter a series of numerical data points separated by spaces: ").split()
    nums_list = []


    for i in num_data_points:
        nums_list.append(float(i))

    print("\nThank you for providing the data points.")
    result = sum_average(nums_list)
    sum = result[0]
    average = result[1]

    print("The sum of the numbers is:", sum)
    print("The average of the numbers is:", average) 


if __name__ == '__main__':
    main()

