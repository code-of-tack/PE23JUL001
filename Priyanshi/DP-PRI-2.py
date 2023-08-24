'''
You are part of a team developing an AI-powered language learning platform called "LinguaTech."
As part of this platform, you have been assigned the task of creating a feature that helps
language learners analyze and improve their pronunciation skills by counting the number of vowels
in a given sentence. This feature will assist learners in identifying vowel sounds, practicing 
their pronunciation, and achieving better fluency in the target language.

'''
def count_vowels(sentence):
    '''
    Calculates the count of vowels
    Args:
        Sentence : String for which we need to count vowels
    Returns:
        int:vowel_count
     
    '''
    vowels="aeiouAEIOU"
    vowel_count=0
    for char in sentence:
        if char in vowels:
            vowel_count+=1

    return vowel_count
def main():
    '''
    Main function to run LinguaTech Pronunciation Analyzer
    '''
    print("Welcome to LinguaTech Pronunciation Analyzer!")
    sentence = input("Please enter a sentence to count the number of vowels:\n")
    vowel_count=count_vowels(sentence)
    print(f"\nThank you for providing the sentence.")
    print(f'The sentence "{sentence}" contains {vowel_count} vowels.')

if __name__ == "__main__":
    main()
