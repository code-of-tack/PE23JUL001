"""
You are part of a team developing a text analysis tool called "TextInsight." As part of this tool, you have been
assigned the task of creating a feature that allows users to analyze the frequency of characters in a given text.
This feature will assist users in understanding the distribution of characters and identifying patterns within the text,
which can be helpful for tasks such as language analysis, cryptography, or data validation.
To accomplish this, you decide to create a program that takes a string as input and
counts the number of occurrences of each character in the string.
The program will provide users with a character frequency analysis,
along with additional functionality to enhance their text analysis capabilities.
"""


def analyze_character_frequency(text):
    # Create a dictionary to store character frequencies
    char_frequency = {}

    # Count the frequency of each character
    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency


def main():
    print("Welcome to TextInsight Character Frequency Analysis!")
    text_input = input("Please enter the text you would like to analyze: ")

    frequency_analysis = analyze_character_frequency(text_input)
    print("\nThank you for providing the text for analysis.")
    print("Here is the character frequency analysis:")
    for char, frequency in frequency_analysis.items():
        print(f"- '{char}' occurs {frequency} time {'s' if frequency > 1 else ''}")


if __name__ == "__main__":
    main()
