// // calculate the sum and average 
function calculateSumAndAverage(dataPoints) {
    // Split the input string into an array of numbers
    const numbers = dataPoints.split(' ').map(Number);
  
    // Calculate the sum of the numbers
    const sum = numbers.reduce((acc, num) => acc + num, 0);
  
    // Calculate the average of the numbers
    const average = sum / numbers.length;
  
    // Return an object containing the sum and average
    return {
      sum,
      average
    };
  }
  
  // Function to prompt the user for input and display the results
  const prompt = require("prompt-sync")({sigint: true});
  function processDataPoints() {
    const dataPoints = prompt('Please enter a series of numerical data points separated by spaces:');
    
    // Check if input is provided
    if (dataPoints.trim() === '') {
      console.log('No data points provided.');
      return;
    }
    
    // Calculate the sum and average
    const result = calculateSumAndAverage(dataPoints);
    
    // Display the results
    console.log('Thank you for providing the data points.');
    console.log('The sum of the numbers is:', result.sum);
    console.log('The average of the numbers is:', result.average.toFixed(2));
  }
  
  // Call the function to start the program
  processDataPoints();

