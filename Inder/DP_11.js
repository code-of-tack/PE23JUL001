/*You are part of a team developing a language processing and sentiment analysis tool for a popular 
social media platform called "SocialConnect." As part of this tool, you have been assigned the task of creating a feature 
that allows users to check if a given string is a palindrome or not. This feature will enable users to analyze and 
interpret user-generated content, such as comments or posts, and identify palindromic patterns that could impact sentiment analysis and user engagement.

To accomplish this, you decide to create a program that checks if a given string is a palindrome or not. 
The program will provide users with immediate feedback regarding the palindromic nature of the input, 
along with additional functionality to enhance their language analysis capabilities. */


function isPalindrome(string) {
    const formattedStr = string.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  
    const reversedStr = formattedStr.split('').reverse().join('');
  
    return formattedStr === reversedStr;
  }
  
  
  
  function palindrom(){
    const inputStr = prompt("Please enter a string to check if it's a palindrome:")
  
    if(inputStr.trim() === ''){
        console.log('No string provided.');
        return;
    }
  
    const isPal = isPalindrome(inputStr);
    
    console.log('Thank you for the providing the string');
    console.log(`The string "${inputStr}" is ${isPal ? '': ' not'} palindrome`);
  
  }
  
  palindrom();