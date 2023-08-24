# Saakshi_DP-01_7/8/23
# You are part of a team developing an advanced financial analytics platform for a 
# leading investment firm called "QuantFinTech." As part of this platform, you have been assigned 
# the task of creating a feature that allows investment analysts to quickly calculate the sum and average 
# of a series of numerical data points. This feature will assist analysts in assessing the performance of 
# investment portfolios, evaluating risk factors, and making informed investment decisions.

# To accomplish this, you decide to create a program that prompts the user to enter a series of numbers separated 
# by spaces and then prints the sum and average of those numbers. The program will provide analysts with valuable 
# statistical information, along with additional functionality to enhance their financial analysis capabilities.


def get_sum_avg(values):
    """
        function that takes in an iterable as an input and returns both ,
        the sum and the average in the following manner.
                return sum, average 
                
    """
    req_sum = sum(values)
    req_avg = req_sum/len(values)
    
    return req_sum, req_avg


def main():
    print("Welcome to QuantFinTech Data Analytics!")
    
    numbers = list(
        map(float, ((input("Please enter a series of numerical data points separated by spaces: ")).split())))

    req_sum, req_avg = get_sum_avg(values=numbers)

    print("\nThank you for providing the data points")
    print("The sum of the numbers is: ", req_sum)
    print("The average of the numbers is: ", req_avg)


if __name__ == '__main__':
    main()
