"""Here is the problem statement for August 16th
You are part of a team developing a text analysis tool called "TextInsight." 
As part of this tool, you have been assigned the task of creating a feature that allows users to analyze the frequency of characters in a given text. 
This feature will assist users in understanding the distribution of characters and identifying patterns within the text, 
which can be helpful for tasks such as language analysis, cryptography, or data validation."""

def count_frequency(text):
    """
    Analyzes the frequency of characters in a given text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary containing the character frequencies.
    """
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def main():
    """
    Main function to run the TextInsight Character Frequency Analysis feature.
    """
    print("Welcome to TextInsight Character Frequency Analysis!")

    user_text = input("Please enter the text you would like to analyze: ")

    freq_count = count_frequency(user_text)
    
    print("\nThank you for providing the text for analysis.")
    print("Here is the character frequency analysis:")
    for character, count in freq_count.items():
        if count == 1:
            print(f"- '{character}' occurs {count} time")
        else:
            print(f"- '{character}' occurs {count} times")

if __name__ == "__main__":
    main()
