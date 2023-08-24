'''
You are part of a team developing a mobile gaming app called "DiceMaster." As part of this
app,you have been assigned the task of creating a feature that simulates a simple dice game, 
providing users with an entertaining experience while also allowing them to improve their
mathematical skills.

'''
import random
def random_number_generator():
    '''
     Generate a random number from a range of 1 to 6.

    Args:
        no arguements

    Returns:
        int: a number from 1 to 6
    '''
    val = random.randint(1, 6) 
    return val
def sum(n1 ,n2):
    '''
    Generate sum of two numbers.

    Args:
        n1(int), n2(int)

    Returns:
        int: sum of two given numbers(val1 + val2)
    '''
    return n1+n2
def main():
    '''
    Main function to run the DiceMaster Dice Game.
    '''
    print("Welcome to DiceMaster Dice Game!")
    print(input("Press the 'Roll' button to roll the dice:"))
    
    n1 = random_number_generator()
    n2 = random_number_generator()
    sum_of_values = sum(n1, n2)

    print("\nThank you for rolling the dice.")
    print(f"You rolled a {n1} and a {n2}. The sum is {sum_of_values}.")

if __name__ == '__main__':
    main()