"""Here is the problem statement for Aug 17th
You are part of a team developing a language learning platform called "WordMaster." 
As part of this platform, you have been assigned the task of creating a feature that allows users to analyze 
and understand the complexity of different texts by counting the number of words in a given file. 
This feature will assist users in improving their vocabulary, assessing text difficulty, and tracking their reading progress."""

def count_words(file):
    """
    Counts the total number of words in a file

    Args:
        file: file path input by user
    
    Returns:
        word_count(int): number of words in the file
    """
    word_count = 0
    
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            word_count += len(words)
    return word_count

def main():
    """
    Main function to run the WordMaster file's word counter feature
    """
    print("Welcome to WordMaster Word Count Analysis!")
    
    file = input("Please enter the path to the file you want to analyze:\n")

    words_count = count_words(file)

    print("\nThank you for providing the file for analysis.")
    print(f"The file contains {words_count} words.")
            
if __name__ == '__main__':
    main()