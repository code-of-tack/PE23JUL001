"""
You are part of a team developing a mobile gaming app called "DiceMaster."
As part of this app, you have been assigned the task of creating a feature that simulates a simple dice game,
providing users with an entertaining experience while also allowing them to improve their mathematical skills.
To accomplish this, you decide to create a program that simulates a simple dice game where the user rolls two dice,
and the program prints the sum of the two numbers.
The program will provide users with the sum, along with additional functionality to enhance their gaming experience.
"""
import random

def dice_game():
    #simulate rolling dice
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total_sum = dice_1 + dice_2 #add both the output of dice
    return [dice_1, dice_2, total_sum]

def main():
    #main function
    print("Welcome to DiceMaster Dice Game!")
    input("Press the 'Roll' button to roll the dice:")
    dice_1, dice_2, total_sum = dice_game()
    print("\nThank you for rolling the dice.")
    print(f"You rolled a {dice_1} and a {dice_2}. The sum is {total_sum}.")

if __name__ == "__main__":
    main()