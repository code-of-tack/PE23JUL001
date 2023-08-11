"""
You are part of a team developing an online marketplace called "MarketSquare."
As part of this marketplace, you have been assigned the task of creating a feature
that allows sellers to manage their product listings effectively.
One essential aspect of product management is sorting the product names in alphabetical order
to ensure consistency and improve searchability for potential buyers.
To accomplish this, you decide to create a program that takes a list of strings as input and sorts them in alphabetical order.
The program will provide sellers with a sorted list of product names,
along with additional functionality to enhance their product management capabilities.

"""

def sort_product(products):

    sorted_products = sorted(products) #sort the list
    return sorted_products

def main():

    print("Welcome to MarketSquare Product Management!")

    # using split function to convert input string into list
    products = input("Please enter your product names, separated by commas:").split(",")


    sorted_products = sort_product(products)

    for name in sorted_products:
        print("-", name)

    print("\nThank you for providing the product names.\n")
    print("Here is the sorted list of product names:\n")

if __name__ == "__main__":
    main()
