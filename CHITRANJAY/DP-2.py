"""
You are part of a team developing an AI-powered language learning platform called "LinguaTech."
As part of this platform, you have been assigned the task of creating a feature that helps language learners analyze and
improve their pronunciation skills by counting the number of vowels in a given sentence.
This feature will assist learners in identifying vowel sounds, practicing their pronunciation,
and achieving better fluency in the target language.
To accomplish this, you decide to create a Python program that takes a sentence as input and
counts the number of vowels (a, e, i, o, u) in the sentence.
The program will provide learners with valuable information about the vowel distribution,
along with additional functionality to enhance their language learning experience.
"""

def count_vowel(sentence):
    """ calculate the count of vowels in the given sentence
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    """  Main function to run LinguaTech Pronunciation Analyzer"""

    print("Welcome to LinguaTech Pronunciation Analysis!")
    input_sentence = input("Please enter a sentence: ")

    vowel_count = count_vowel(input_sentence)
    print("\nVowel analysis complete:")
    print(f"Number of vowels in the sentence: {vowel_count} vowels.")

if __name__ == "__main__":
    main()