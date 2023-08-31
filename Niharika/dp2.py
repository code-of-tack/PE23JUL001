def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count

def main():
    print("Welcome to LinguaTech Pronunciation Analyzer!")
    sentence = input("Please enter a sentence to count the number of vowels:\n")

    num_vowels = count_vowels(sentence)
    print(f"Thank you for providing the sentence.")
    print(f"The sentence \"{sentence}\" contains {num_vowels} vowels.")

if __name__ == "__main__":
    main
        
        
