/* You are part of a team developing a search engine called "Searchify." As part of this search engine, 
you have been assigned the task of creating a feature that implements a binary search algorithm to efficiently 
find a specific element in a sorted list of data. This feature will assist users in searching for specific information, 
retrieving relevant results quickly, and improving the overall search experience. */

// Function to perform binary search on a sorted list
function binarySearch(list, value) {
    let left = 0;
    let right = list.length - 1;
  
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
  
      if (list[mid] === value) {
        return mid; // Element found, return its index
      } else if (list[mid] < value) {
        left = mid + 1; // Search the right half of the list
      } else {
        right = mid - 1; // Search the left half of the list
      }
    }
  
    return -1; // Element not found
  }
  
  // Function to handle user input and display the search result
  function main() {
    console.log("Welcome to Searchify!");
    console.log("Please enter the element you want to search for:");
  
    // Read user input from the command line or any other input mechanism
    const sortedList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]; // Replace this line with the actual sorted list
    const val = 42; // value to be searched in the sorted list
  
    // Call the binarySearch function to find the element in the list
    const result = binarySearch(sortedList, val);
  
    // Display the search result
    console.log("Thank you for providing the search element.");
  
    if (result !== -1) {
      console.log("The element " + searchElement + " was found at index " + result + ".");
    } else {
      console.log("The element " + searchElement + " was not found in the list.");
    }
  }
  
  // Call the main function to start the search feature
  main();

