"""Problem Statement for Aug 21st
You are part of a team developing a language processing and sentiment analysis tool for a popular 
social media platform called "SocialConnect." As part of this tool, you have been assigned the task of creating a feature 
that allows users to check if a given string is a palindrome or not. This feature will enable users to analyze and 
interpret user-generated content, such as comments or posts, and identify palindromic patterns that could impact sentiment analysis and user engagement."""

def is_palindrome(str):
    """
    Checks if a given string is a palindrome.

    Args:
        str (string): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_str = ''.join(str.split()).lower()  # Remove spaces and convert to lowercase

    return cleaned_str == cleaned_str[::-1]     # Check if the cleaned string is equal to its reverse


def main():
    """
    Main function to run the palindrome checker program.
    """
    print("Welcome to SocialConnect Language Analysis!")
    input_string = input("Please enter a string to check if it's a palindrome:\n")

    if is_palindrome(input_string) is True:
        print(f'Thank you for providing the string.\nThe string "{input_string}" is a palindrome.')
    
    else:
        print(f'Thank you for providing the string.\nThe string "{input_string}" is not a palindrome.')


if __name__ == "__main__":
    main()