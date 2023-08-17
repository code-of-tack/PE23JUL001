/*You are part of a team developing a text analysis tool called "TextInsight." As part of this tool, you have been 
assigned the task of creating a feature that allows users to analyze the frequency of characters in a given text.
 This feature will assist users in understanding the distribution of characters and identifying patterns within the text,
 which can be helpful for tasks such as language analysis, cryptography, or data validation. */


function analyzeCharacterFrequency(text) {
    /* function for analyze frequency of characters.
    args:
        text = text entered by user.
    returns:
        return the frequency count of the character. */
    
    const frequencyMap = new Map();

    // Remove spaces and convert text to lowercase for case-insensitive analysis
    const cleanedText = text.replace(/\s/g, '').toLowerCase();

    // Count character occurrences
    for (const char of cleanedText) {
        if (frequencyMap.has(char)) {
            frequencyMap.set(char, frequencyMap.get(char) + 1);
        } else {
            frequencyMap.set(char, 1);
        }
    }

    return frequencyMap;
}

function displayCharacterFrequencyAnalysis(frequencyMap) {
    /* function for display the frequency of character.
    args:
        frequency map return by analyzeCharacterFrequency function.
    returns:
        no return. */
    
    console.log("Here is the character frequency analysis:");
    
    frequencyMap.forEach((count, char) => {
        console.log(`- '${char}' occurs ${count} time${count > 1 ? 's' : ''}`);
    });
}


const prompt = require("prompt-sync")({sigint: true});
console.log("Welcome to TextInsight Character Frequency Analysis!");
const text = prompt("Please enter the text you would like to analyze:");
const frequencyMap = analyzeCharacterFrequency(text);
console.log(`Thank you for providing the text for analysis.`);
displayCharacterFrequencyAnalysis(frequencyMap);

