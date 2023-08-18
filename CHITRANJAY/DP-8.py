"""
You are part of a team developing a language learning platform called "WordMaster."
As part of this platform, you have been assigned the task of creating a feature that allows users to analyze and
understand the complexity of different texts by counting the number of words in a given file.
This feature will assist users in improving their vocabulary,
assessing text difficulty, and tracking their reading progress.
To accomplish this, you decide to create a program that reads a file and counts the number of words in the file.
The program will provide users with the word count,
along with additional functionality to enhance their text analysis capabilities.
"""


def word_count_analysis(file_path):
    #using try block for locating the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count

    except FileNotFoundError:
        return -1

def main():
    #main function for execution
    print("Welcome to WordMaster Word Count Analysis!")
    file_path = input("Please enter the path to the file you want to analyze: ")

    word_count = word_count_analysis(file_path)
    if word_count >= 0:
        print("\nThank you for providing the file for analysis.")
        print(f"The file contains {word_count} word{'s' if word_count != 1 else ''}.")
    else:
        print("\nThe provided file path does not exist.")


if __name__ == "__main__":
    main()
