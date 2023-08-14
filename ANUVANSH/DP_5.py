import random

def generate_random_num():
    """
    Generate a random number from a range of 1 to 6.

    Args:
        no arguements

    Returns:
        int: a number from 1 to 6
    """
    value = random.randint(1, 6) 
    return value


def sum(val1, val2):
    """
    Generate sum of two numbers.

    Args:
        val1(int), val2(int)

    Returns:
        int: sum of two given numbers(val1 + val2)
    """
    return val1 + val2

def main():
    """
    Main function to run the DiceMaster Dice Game.
    """
    print("Welcome to DiceMaster Dice Game!")
    print(input("Press the 'Roll' button to roll the dice:"))
    
    dice1_value = generate_random_num()
    dice2_value = generate_random_num()
    sum_of_values = sum(dice1_value, dice2_value)

    print("\nThank you for rolling the dice.")
    print(f"You rolled a {dice1_value} and a {dice2_value}. The sum is {sum_of_values}.")

if __name__ == '__main__':
    main()
