def reverse_string(input_string):
    return input_string[::-1]

def main():
    print("Welcome to RevShare Quote Sharing!")
    user_quote = input("Please enter your quote:\n")

    reversed_quote = reverse_string(user_quote)

    print("\nThank you for sharing your quote.")
    print(f"Here is your quote in reverse: \"{reversed_quote}\"")

if __name__ == "__main__":
    main()
