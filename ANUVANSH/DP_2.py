"""Problem statement for August 8th(DP-2)
You are part of a team developing an AI-powered language learning platform called "LinguaTech." 
As part of this platform, you have been assigned the task of creating a feature that helps language learners analyze and improve
their pronunciation skills by counting the number of vowels in a given sentence.
This feature will assist learners in identifying vowel sounds, practicing their pronunciation, 
and achieving better fluency in the target language."""

def vowels_counter(sentence):
    """
       Counts the number of vowels in a sentence.

       Args:
            sentence (string): The sentence for which number of vowels has to be counted.
       
       Returns:
            int: Number of vowels in the given sentence
    """
    vowels = 'aeiouAEIOU'
    vowel_count = 0

    for character in sentence:
        if character in vowels:
            vowel_count += 1
    
    return vowel_count


def main():
    """
        Main fucntion to run the LinguaTech - Vowel Counter Feature.
    """
    print("Welcome to LinguaTech Pronunciation Analyzer!")

    sentence = input("Please enter a sentence to count the number of vowels:\n")

    no_of_vowels = vowels_counter(sentence)

    print("\nThank you for providing the sentence.")
    print(f"The sentence \"{sentence}.\" contains {no_of_vowels} vowels.")

#Run the main() program
if __name__ == "__main__":
    main()
