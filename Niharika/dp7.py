def character_frequency_analysis(text):
    character_count = {}
    
    # Count the occurrences of each character in the text
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    
    # Display the character frequency analysis
    print("Thank you for providing the text for analysis.")
    print("Here is the character frequency analysis:")
    for char, count in character_count.items():
        print(f"- '{char}' occurs {count} time{'s' if count > 1 else ''}")

# Main program
print("Welcome to TextInsight Character Frequency Analysis!")
input_text = input("Please enter the text you would like to analyze: ")
character_frequency_analysis(input_text)
