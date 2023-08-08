// You are part of a team developing an AI-powered language learning platform called "LinguaTech."
//As part of this platform, you have been assigned the task of creating a feature that helps
//language learners analyze and improve their pronunciation skills by counting the number of vowels
//in a given sentence. This feature will assist learners in identifying vowel sounds, practicing 
//their pronunciation, and achieving better fluency in the target language.

// function for count vowels
// vowelCount : calculates the count of vowels 
// Sentence : String for which we need to count vowels
function countVowels(sentence) {
    const vowels = "aeiouAEIOU";
    let vowelCount = 0;
    
    for (let char of sentence) {
      if (vowels.includes(char)) {
        vowelCount++;
      }
    }
    
    return vowelCount;
  }
  
  console.log("Welcome to LinguaTech Pronunciation Analyzer!");
  const sentence = prompt("Please enter a sentence to count the number of vowels: ");
  const vowelCount = countVowels(sentence);
  console.log(`Thank you for providing the sentence.`);
  console.log(`The sentence "${sentence}" contains ${vowelCount} vowels.`);
  