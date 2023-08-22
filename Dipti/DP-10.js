/*You are part of a team developing a language processing and sentiment analysis tool for a popular social media 
platform called "SocialConnect."As part of this tool, you have been assigned the task of creating a feature 
that allows users to check if a given string is a palindrome or not. This feature will enable users to analyze and 
interpret user-generated content, such as comments or posts, and identify palindromic patterns that could impact 
sentiment analysis and user engagement. */

// Function to check if a string is a palindrome
function isPalindrome(str) {
    // Remove spaces and punctuation from the string and convert to lowercase
    const formattedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  
    // Reverse the string
    const reversedStr = formattedStr.split('').reverse().join('');
  
    // Check if the reversed string is equal to the original string
    return formattedStr === reversedStr;
  }
  
  // Function to prompt the user for input and check if it's a palindrome
  function processStringPalindrome() {
    const inputStr = prompt('Please enter a string to check if it\'s a palindrome:');
    
    // Check if input is provided
    if (inputStr.trim() === '') {
      console.log('No string provided.');
      return;
    }
    
    // Check if the string is a palindrome
    const isPal = isPalindrome(inputStr);
    
    // Display the result
    console.log('Thank you for providing the string.');
    console.log(`The string "${inputStr}" is${isPal ? '' : ' not'} a palindrome.`);
  }
  
  // Call the function to start the program
  processStringPalindrome();