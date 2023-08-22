/* You are part of a team developing a language learning platform called "WordMaster."
 As part of this platform, you have been assigned the task of creating a feature that allows users to analyze and 
 understand the complexity of different texts by counting the number of words in a given file. This feature will 
assist users in improving their vocabulary, assessing text difficulty, and tracking their reading progress. */

const fs = require('fs');

// Function to calculate the word count in a file
function countWordsInFile(filePath) {
  try {
    // Read the file content
    const fileContent = fs.readFileSync(filePath, 'utf8');

    // Split the content into words using whitespace as the delimiter
    const words = fileContent.split(/\s+/);

    // Filter out empty words
    const filteredWords = words.filter(word => word !== '');

    // Return the word count
    return filteredWords.length;
  } catch (error) {
    throw new Error('Error reading file: ' + error.message);
  }
}

// Function to handle user input and display the result
function wordCountAnalysis() {
  console.log("Welcome to WordMaster Word Count Analysis!");
  console.log("Please enter the path to the file you want to analyze:");

  // Read user input from the command line or any other input mechanism
  const userInput = "path/to/myfile.txt"; // Replace this line with actual user input

  // Call the countWordsInFile function to calculate the word count
  try {
    const result = countWordsInFile(userInput);

    // Display the result
    console.log("Thank you for providing the file for analysis.");
    console.log("The file contains " + result + " words.");
  } catch (error) {
    console.log(error.message);
  }
}

// Call the wordCountAnalysis function to start the word count analysis tool
wordCountAnalysis();