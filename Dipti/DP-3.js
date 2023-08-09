// You are part of a team developing a financial planning application called "FinPlanPro." As part of this application,
//  you have been assigned the task of creating a feature that generates the Fibonacci sequence up to a given number 'n'.
//  This feature will assist financial planners and investment advisors in performing calculations 
// related to interest rates, asset growth, and investment strategies.

function fibonaccci_series(n)
{
    const fibonaccisequence = [2, 1];
    while(fibonaccisequence[fibonaccisequence.length-1] + fibonaccisequence[fibonaccisequence.length-2] <= n)
    {
        fibonaccisequence.push(fibonaccisequence[fibonaccisequence.length-1] + fibonaccisequence[fibonaccisequence.length-2]);
    }
    return fibonaccisequence;
}
const prompt = require("prompt-sync")({sigint: true});
console.log("Welcome to FinPlanPro Fibonacci Generator!");
const n = prompt("Please enter the desired number 'n' to generate the Fibonacci sequence: ");
const fibonaccisequence = fibonaccci_series(n);
console.log("Thank you for providing the number 'n'.");
console.log(`The Fibonacci sequence up to ${n} is: ${fibonaccisequence.join(', ')} `);