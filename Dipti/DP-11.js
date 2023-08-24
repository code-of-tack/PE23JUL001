/* You are part of a team developing a data analytics platform 
called "DataMetrics." As part of this platform, you have been 
assigned the task of creating a feature that allows users to 
read a CSV (Comma-Separated Values) file and calculate the 
average of a specific column. 
This feature will enable data analysts and business professionals 
to quickly analyze numerical data, gain insights, and make data-driven decisions. */

// run 'npm install csv-parser fs' install the module csv-parser filesystem to work on the csv file.

const fs = require('fs');
const csv = require('csv-parser');

// Function to calculate the average of a specific column
function calculateAverage(data, columnName) {
  const columnData = data.map(row => parseFloat(row[columnName])).filter(value => !isNaN(value));
  
  if (columnData.length === 0) {
    return null;
  }

  const sum = columnData.reduce((acc, value) => acc + value, 0);
  const average = sum / columnData.length;

  return average;
}

// Function to read and analyze the CSV file
function analyzeCSV(filePath, columnName) {
  const results = [];

  fs.createReadStream(filePath)
    .pipe(csv())
    .on('data', data => results.push(data))
    .on('end', () => {
      const average = calculateAverage(results, columnName);
      if (average !== null) {
        console.log(`Thank you for providing the CSV file.`);
        console.log(`The average value of the '${columnName}' column is: $${average.toFixed(2)}.`);
      } else {
        console.log(`No valid data found in the specified column.`);
      }
    });
}

// Entry point
console.log("Welcome to DataMetrics Data Analytics!");
const filePath = prompt("Please enter the path or name of the CSV file: ");
const columnName = prompt("Please enter the name of the column you want to analyze: ");

analyzeCSV(filePath, columnName);
