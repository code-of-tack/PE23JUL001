// Function to calculate the sum of an array of numbers
function calculateSum(data) {
  return data.reduce((acc, num) => acc + num, 0);
}

// Function to calculate the average of an array of numbers
function calculateAverage(data) {
  const sum = calculateSum(data);
  return sum / data.length;
}

// Function to process user input and display the results
function processData(input) {
  const dataPoints = input.split(" ").map(Number);
  const sum = calculateSum(dataPoints);
  const average = calculateAverage(dataPoints);

  console.log("Thank you for providing the data points.");
  console.log("The sum of the numbers is:", sum.toFixed(2));
  console.log("The average of the numbers is:", average.toFixed(2));
}

// Example usage:
const userInput = prompt("Welcome to QuantFinTech Data Analytics!\nPlease enter a series of numerical data points separated by spaces:");
processData(userInput);


