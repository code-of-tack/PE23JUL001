/*You are part of a team developing a language processing and sentiment analysis tool for a popular 
social media platform called "SocialConnect." As part of this tool, you have been assigned the task of creating a feature 
that allows users to check if a given string is a palindrome or not. This feature will enable users to analyze and 
interpret user-generated content, such as comments or posts, and identify palindromic patterns that could impact sentiment analysis and user engagement.

To accomplish this, you decide to create a program that checks if a given string is a palindrome or not. 
The program will provide users with immediate feedback regarding the palindromic nature of the input, 
along with additional functionality to enhance their language analysis capabilities. */


function checkpalindrome(string) {
    let temp = string.toLowerCase();
    let newString = string.split("").reverse().join("").toLowerCase();    

    if(temp == newString){
        return true;
    }
}



function palindrom(){
    console.log('Welcome to SocialConnect Language Analysis!');
    console.log("Please enter a string to check if it's a palindrome:");

    const string = prompt("Enter the string");
    
    if(string){
        console.log('Thank you for the providing the string');
        const result = checkpalindrome(string);

        if(result){
             console.log(`The string "${string}" is palindrome`);
        }
        else {
             console.log(`The string "${string}" is not palindrome`)
        }
    }

}

palindrom();