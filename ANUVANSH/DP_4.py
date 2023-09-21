"""Here is the problem statement for Aug 10th
You are part of a team developing an online marketplace called "MarketSquare." 
As part of this marketplace, you have been assigned the task of creating a feature
that allows sellers to manage their product listings effectively. 
One essential aspect of product management is sorting the product names in alphabetical order 
to ensure consistency and improve searchability for potential buyers."""

def sort_product_names(str_list):
    """
    Generate the Sorted list of Product names in Alphabetical order.

    Args:
        str_list (list of strings): The list of products

    Returns:
        list[strings]: The sorted list of product names
    """
    
    str_list.sort()
    return str_list
    

def main():
    """
    Main Function to run the MarketSquare Sorted Product Names Generator.
    """
    print("Welcome to MarketSquare Product Management!")
    product_names = input("Please enter your product names, separated by commas: \n").split(',')

    sorted_product_names = sort_product_names(product_names)

    print("\nThank you for providing the product names.")
    print("Here is the sorted list of product names:")

    for name in sorted_product_names:   #Prints the product names from sorted_product_names list in the desired format, 
        print('-', format(name))        #that is every name on new line starting with '-'


if __name__ == "__main__":
    main()
    

