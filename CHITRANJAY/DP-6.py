"""
You are part of a team developing a social media platform called "RevShare."
As part of this platform, you have been assigned the task of creating a feature that allows users to share and discover inspiring quotes.
One essential aspect of quote sharing is the ability to present quotes in a visually appealing and engaging manner,
including displaying quotes in reverse order to add a unique touch.
To accomplish this, you decide to create a program that takes a string as input and prints the reverse of the string.
The program will provide users with the reversed string,
along with additional functionality to enhance their quote sharing experience.
"""

def quote_sharing():
    print("Welcome to RevShare Quote Sharing!")
    quote = input("Please enter your quote:")

    print("Thank you for sharing your quote.")

    #reverse the string of quote
    reversed_quote = quote[::-1]
    print(f"Here is your quote in reverse:{reversed_quote}")

if __name__ == "__main__":
    quote_sharing()