/* You are part of a team developing a scientific calculator called "CalcPro." As part of this calculator, 
you have been assigned the task of creating a feature that calculates the factorial of a given number. 
This feature will assist users in performing complex mathematical calculations, solving mathematical problems, 
and analyzing data in various scientific disciplines.*/

// function to claculate the factorial of number .
function calculate_fact(number)
{
    if (number < 0) {
        throw new Error('Factorial is not defined for negative numbers.');
      }
    
      let factorial = 1;
    
      // Multiply the factorial by each number from 1 to the input number
      for (let i = 1; i <= number; i++) {
        factorial *= i;
      }
    
      // Return the factorial value
      return factorial;
    
}

// function to handle user input and display result.
function main()
{
    const prompt = require("prompt-sync")({sigint: true});
    console.log("Welcome to CalcPro Factorial Calculation!");
    let num = prompt("Please enter the number for which you want to calculate the factorial:");
    let factorial = calculate_fact(num);
    console.log("Thank you for providing the number for factorial calculation.");
    console.log(`The factorial of "${num}" is "${factorial}"`);
}
main();