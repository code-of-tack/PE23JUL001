"""
You are part of a team developing an e-commerce platform called "ShopSmart."
As part of this platform, you have been assigned the task of creating a feature that helps users
to find the second-largest price among a list of products.
This feature will assist users in making informed purchasing decisions,
comparing prices, and identifying the best deals available.
To accomplish this, you decide to create a program that takes a list of integers as input,
representing the prices of different products, and finds the second-largest number in the list.
The program will provide users with the second-largest price,
along with additional functionality to enhance their shopping experience.
"""


def find_second_largest_price(prices):
    if len(prices) < 2:
        return "Not enough prices to find the second-largest."

    prices = [9.99, 14.99, 24.99, 19.99, 12.99, 29.99, 8.99]

    largest = second_largest = float('-inf')

    for price in prices:
        if price > largest:
            second_largest = largest
            largest = price
        elif price > second_largest and price != largest:
            second_largest = price

    return second_largest


def main():
    """
    Main function to run the ShopSmart Product Browsing feature.
    """
    print("Welcome to ShopSmart Product Browsing!")

    prices = [9.99, 14.99, 24.99, 19.99, 12.99, 29.99, 8.99]

    print("Here are the prices of the available products:")
    print(prices)

    second_largest_price = find_second_largest_price(prices)
    print("The second-largest price is:", second_largest_price)


if __name__ == "__main__":
    main()