'''
You are part of a team developing a text analysis tool called "TextInsight."
As part of this tool, you have been assigned the task of creating a feature
that allows users to analyze the frequency of characters in a given text. 
This feature will assist users in understanding the distribution of characters
and identifying patterns within the text, which can be helpful for tasks such 
as language analysis, cryptography, or data validation.
'''
def character_frequency_analysis(text):
    '''
    Args:
       text:string which needs to be reversed

    '''

    char_frequency = {}

    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1


    print("Thank you for providing the text for analysis.")
    print("Here is the character frequency analysis:")
    for char, freq in char_frequency.items():
        print(f"- '{char}' occurs {freq} time{'s' if freq > 1 else ''}")

def main():
    '''
    Main function for character frequency analysis
    '''
    print("Welcome to TextInsight Character Frequency Analysis!")
    text_input = input("Please enter the text you would like to analyze:\n")
    character_frequency_analysis(text_input)

if __name__ == "__main__":
    main()
