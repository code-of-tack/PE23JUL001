import random

def roll_dice():
    # Simulate rolling two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    # Calculate the sum of the dice
    total = dice1 + dice2
    
    return dice1, dice2, total

def main():
    print("Welcome to DiceMaster Dice Game!")
    print("Press the 'Roll' button to roll the dice:")
    
    while True:
        user_input = input("Press 'R' to roll the dice or 'Q' to quit: ").upper()
        
        if user_input == 'R':
            dice1_result, dice2_result, total_result = roll_dice()
            print(f"Thank you for rolling the dice.")
            print(f"You rolled a {dice1_result} and a {dice2_result}. The sum is {total_result}.\n")
        elif user_input == 'Q':
            print("Thank you for playing DiceMaster Dice Game!")
            break
        else:
            print("Invalid input. Press 'R' to roll or 'Q' to quit.\n")

if __name__ == "__main__":
    main()
