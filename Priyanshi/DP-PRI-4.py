'''
You are part of a team developing an online marketplace called "MarketSquare."
As part of this marketplace, you have been assigned the task of creating a 
feature that allows sellers to manage their product listings effectively. One
essential aspect of product management is sorting the product names in alphabetical 
order to ensure consistency and improve searchability for potential buyers.

'''
def manage_product_listings():
    '''
    function use to sort elements in sorted list
    '''
    print("Welcome to MarketSquare Product Management!")
    input_names = input("Please enter your product names, separated by commas: ")
    product_names = [name.strip() for name in input_names.split(",")]
    sorted_names = sorted(product_names)

    print("\nThank you for providing the product names.")
    print("Here is the sorted list of product names:")
    for name in sorted_names:
        print("-", name)

def main():
    manage_product_listings()

if __name__ == "__main__":
    main()
