"""
You are part of a team developing a language processing and sentiment analysis tool
for a popular social media platform called "SocialConnect."
As part of this tool, you have been assigned the task of creating a feature
that allows users to check if a given string is a palindrome or not. This feature will enable users to analyze and
interpret user-generated content, such as comments or posts,
and identify palindromic patterns that could impact sentiment analysis and user engagement.
To accomplish this, you decide to create a program that checks if a given string is a palindrome or not.
The program will provide users with immediate feedback regarding the palindromic nature of the input,
along with additional functionality to enhance their language analysis capabilities.
"""


def pallindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse


def main():

    # Get input from the user
    print("Welcome to SocialConnect Language Analysis!\n")
    input_string = input("Please enter a string to check if it's a palindrome: ")

    # Check if the input string is a palindrome
    if pallindrome(input_string):
        print(f"The string \"{input_string}\" is a palindrome.")
    else:
        print(f"The string \"{input_string}\" is not a palindrome.")

if __name__ == "__main__":
    main()