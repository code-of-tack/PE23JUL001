"""
You are part of a team developing a social media platform called "RevShare." 
As part of this platform, you have been assigned the task of creating a feature that allows users to share and discover inspiring quotes. 
One essential aspect of quote sharing is the ability to present quotes in a visually appealing and engaging manner, 
including displaying quotes in reverse order to add a unique touch.

"""
def reverse_string(str):
    """
    Reverses the quote(a string).

    Args:
        str(string): The quote that is given by the user

    Returns:
        string: The reversed version of the user's quote
    """
    return(str[::-1])

def main():
    """
    Main function to run the RevShare string reversing feature.
    """
    print("Welcome to RevShare Quote Sharing!")
    user_quote = input("Please enter your quote:\n")

    print("\nThank you for sharing your quote.")
    rev_quote = reverse_string(user_quote)
    
    print(f"Here is your quote in reverse: \"{rev_quote}\"")

if __name__ == "__main__":
    main()