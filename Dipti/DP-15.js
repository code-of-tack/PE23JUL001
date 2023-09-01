/* You are part of a team developing an e-commerce platform called "MarketPro." As part of this platform, 
you have been assigned the task of creating a feature that finds the kth largest element in an unsorted list. 
This feature will assist users in identifying popular products, analyzing sales trends, and optimizing their purchasing 
decisions. */

function findKthLargest(nums, k) {
    // Sort the array in descending order
    nums.sort((a, b) => b - a);
  
    // Return the kth largest element
    return nums[k - 1];
  }
  
  // Function to handle user input and display the kth largest element
  function main() {
    console.log("Welcome to MarketPro - Popular Products!");
    console.log("Please enter the value of k to find the kth largest element:");
  
    // Read user input for k
    const k = parseInt(prompt());
  
    // Create the unsorted list of elements (replace this with your own list)
    const elements = [12, 45, 67, 86, 23, 56, 34, 99];
  
    // Find the kth largest element
    const kthLargest = findKthLargest(elements, k);
  
    // Display the result
    console.log("Thank you for providing the value of k.");
    console.log("The kth largest element is:", kthLargest);
  }
  
  // Call the main function to start the Popular Products feature
  main();