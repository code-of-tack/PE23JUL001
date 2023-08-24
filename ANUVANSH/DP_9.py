"""
Here is the problem statement for Aug 18th and Aug 19th
You are part of a team developing an e-commerce platform called "ShopSmart." 
As part of this platform, you have been assigned the task of creating a feature that helps users find the second-largest price among a list of products. 
This feature will assist users in making informed purchasing decisions, comparing prices, and identifying the best deals available.
"""

def second_largest(user_list):
    """
    Returns the second largest element of the given list.

    Args:
        user_list (list): list input by the user

    Returns:
        second_largest_elem (int or float): second largest element in the list
    """
    unique_list = list(set(user_list))
    unique_list.sort()
    
    second_largest_elem = unique_list[-2]
    return second_largest_elem

def main():
    """
    Main function to run the ShopSmart Product Browsing feature.
    """
    product_prices = [9.99, 14.99, 24.99, 19.99, 12.99, 29.99, 8.99]

    print("Welcome to ShopSmart Product Browsing!")
    print("Here are the prices of the available products:")
    print(product_prices)

    second_largest_price = second_largest(product_prices)

    print("\nThe second-largest price is:", second_largest_price)

if __name__ == '__main__':
    main()
