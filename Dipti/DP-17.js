/* You are part of a team developing a recipe recommendation app called "RecipeGenius." As part of this app,
 you have been assigned the task of creating a feature that generates all possible combinations of ingredients
  from a user's pantry. This feature will assist users in discovering new recipe ideas, optimizing their ingredient usage,
   and expanding their culinary repertoire. */

   //generate possible combinations of entered input ingredients by user
   function generateCombinations(ingredients) {
        const results = [];
        
        function backtrack(start, currentCombination) {
        results.push(currentCombination.join(', '));
    
        for (let i = start; i < ingredients.length; i++) {
            currentCombination.push(ingredients[i]);
            backtrack(i + 1, currentCombination);
            currentCombination.pop();
        }
        }
    
        backtrack(0, []);
        return results;
  }


// Function to handle user input and display possible combination.
function main() {
    console.log("Welcome to RecipeGenius - Discover Recipes!");
    const inputNames = prompt("Please enter the ingredients available in your pantry (separated by commas):");
    const ingredients = inputNames.split(',').map(name => name.trim());

    //check whether the ingredients are greater than 2 or not
    if (ingredients.length < 2) {
        console.log('You need at least 2 ingredients to generate combinations.');
      } else {
          //call generatecombinations function to generate possible combinations.
        const combinations = generateCombinations(ingredients);
        console.log('Thank you for providing the ingredients in your pantry.');
        console.log('Here are all possible combinations:');
        combinations.forEach((combination, index) => {
          console.log(`${index + 1}. ${combination}`);
        });
      }
}

// call the main function 
main();