
function reverseString(str)
{
    /*reverse the string
    args: 
        str : input string from the main function.

    return: reverse string. */
    let reverse = ' ';
    for(let i=str.length -1;i>=0;i--)
    {
        reverse += str[i];
    }
    return reverse;
}

// main function for take input from the user 
function main()
{
    const prompt = require("prompt-sync")({sigint: true});
    console.log("Welcome to RevShare Quote Sharing!");
    let userQuote = prompt("Please enter your quote: ");
    let reversedQuote = reverseString(userQuote);
    console.log("Thank you for sharing your quote.");
    console.log(`Here is your quote in reverse: "${reversedQuote}"`);

}
main();