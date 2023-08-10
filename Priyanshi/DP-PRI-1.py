"""
Problem Statement for August 7th(DP-1)
You are part of a team developing an advanced financial analytics platform for a 
leading investment firm called "QuantFinTech." As part of this platform, you have been assigned 
the task of creating a feature that allows investment analysts to quickly calculate the sum and average 
of a series of numerical data points. This feature will assist analysts in assessing the performance of 
investment portfolios, evaluating risk factors, and making informed investment decisions.
"""

def sum(floatnumbers):
    """
    Calculates the sum of a series of numerical data points.
    
       Args:
            floatnumbers (list of floats): The  numbers to be totaled.
       
       Returns:
            float:total
    """
    total = 0

    for i in range(0, len(floatnumbers)):
        total = total + floatnumbers[i]

    return total
def average(result1,n):
    """
    Calculates the average of a series of numerical datapoints.
    
       Args:
            result1: The total of numbers for which we have to calculate average.
            n:length of  the list
       Returns:
            float: The average(avg)
    """
    avg=result1/n    
    return avg


def main():
    """
    Main function to run the QuantFinTech - Sum 
    and Average feature.
    
    """
    numerical_list = []
    print("Welcome to QuantFinTech Data Analytics!")
    
    numerical_datapoints = input("Please enter a series of numerical data points separated by spaces: ").split()
    
    for i in numerical_datapoints:
        numerical_list.append(float(i))
    n=len(numerical_list)
    print("\nThank you for providing the data points.")
    result1 = sum(numerical_list)
    result2 = average(result1,n)
    print("\nThe sum of the numbers is:", result1)
    print("\nThe average of the numbers is:", result2) 


if __name__ == '__main__':
    main()

