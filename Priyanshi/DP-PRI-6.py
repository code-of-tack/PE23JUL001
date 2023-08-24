'''
You are part of a team developing a social media platform called "RevShare." As part 
of this platform, you have been assigned the task of creating a feature that allows
users to share and discover inspiring quotes. One essential aspect of quote sharing 
is the ability to present quotes in a visually appealing and engaging manner, including
displaying quotes in reverse order to add a unique touch.

'''
def reverse_string(input_string):
    '''
    reverse function to reverse string
    Args:
       String : input_string
    Return:
       String:input_string which is reversed
    '''
    return input_string[::-1]

def main():
    '''
    Main Function for RevShare Quote Sharing
    '''
    print("Welcome to RevShare Quote Sharing!")
    user_input = input("Please enter your quote:\n")
    
    reversed_quote = reverse_string(user_input)
    
    print("Thank you for sharing your quote.")
    print(f"Here is your quote in reverse: \"{reversed_quote}\"")

if __name__ == "__main__":
    main()