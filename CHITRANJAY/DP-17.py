"""
You are part of a team developing a recipe recommendation app called "RecipeGenius." As part of this app,
you have been assigned the task of creating a feature that generates all possible combinations of ingredients
from a user's pantry. This feature will assist users in discovering new recipe ideas, optimizing their ingredient usage,
and expanding their culinary repertoire. To accomplish this,
you decide to create a program that takes a list of elements (ingredients) as input and generates
all possible combinations of these elements.
The program will provide users with the combinations,
along with additional functionality to enhance their cooking experience.
"""

from itertools import combinations


# Define a function to generate all possible combinations of ingredients
def generate_combinations(ingredients):
    all_combinations = []
    for r in range(1, len(ingredients) + 1):
        # Use itertools.combinations to generate combinations of different lengths
        combos = combinations(ingredients, r)
        all_combinations.extend(combos)
    return all_combinations


# Main function to interact with the user
def main():
    print("Welcome to RecipeGenius - Discover Recipes!")

    # Input the ingredients from the user (comma-separated)
    input_ingredients = input("Please enter the ingredients available in your pantry (separated by commas): ")

    # Split the input into a list of ingredients
    ingredients = [ingredient.strip() for ingredient in input_ingredients.split(',')]

    # Generate all possible combinations of ingredients
    combinations_list = generate_combinations(ingredients)

    if not combinations_list:
        print("No ingredients provided. Please enter at least one ingredient.")
        return

    print("Thank you for providing the ingredients in your pantry.")
    print("Here are all possible combinations:")

    # Display the combinations
    for combo in combinations_list:
        print('- ' + ', '.join(combo))


if __name__ == "__main__":
    main()
