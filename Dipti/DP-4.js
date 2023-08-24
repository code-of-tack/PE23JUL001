//You are part of a team developing an online marketplace called "MarketSquare." As part of this marketplace, you have been assigned the task of creating a feature that allows sellers to manage their product listings effectively. One essential aspect of product management is sorting the product names in alphabetical order to ensure consistency and improve searchability for potential buyers.

// function for take the product name  from the user and sort them in alphabetical order.
function main() {
    console.log("Welcome to MarketSquare Product Management!");
    // take product name as input that is separated by comma.
    const inputNames = prompt("Please enter your product names, separated by commas:");
    // split the input by comma.
    const productNames = inputNames.split(',').map(name => name.trim());
    // sort the names in alphabetical order.
    const sortedNames = productNames.slice().sort();

    console.log("\nThank you for providing the product names.");
    console.log("Here is the sorted list of product names:");
    sortedNames.forEach(name => console.log(`- ${name}`));
}

main();
