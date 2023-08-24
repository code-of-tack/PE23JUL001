'''
You are part of a team developing a language learning platform called "WordMaster."
As part of this platform, you have been assigned the task of creating a feature
that allows users to analyze and understand the complexity of different texts by
counting the number of words in a given file. This feature will assist users in
improving their vocabulary, assessing text difficulty, and tracking their reading progress.

'''
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def main():
    print("Welcome to WordMaster Word Count Analysis!")
    file_path = input("Please enter the path to the file you want to analyze: ")

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        word_count = count_words(content)
        print("\nThank you for providing the file for analysis.")
        print(f"The file contains {word_count} words.")

if __name__ == "__main__":
    main()
