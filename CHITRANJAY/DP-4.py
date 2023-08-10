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

def product_listing():
    print("Welcome to MarketSquare Product Management!")
    product_input = input("Please enter your product names, separated by commas:")

    #using split function to convert input string into list
    product = [name.strip() for name in product_input.split(',')]

    sorted_products = sorted(product) #sort the list

    print("\nThank you for providing the product names.\n")
    print("Here is the sorted list of product names:\n")
    for name in sorted_products:
        print("-", name)

if __name__ == "__main__":
    product_listing()