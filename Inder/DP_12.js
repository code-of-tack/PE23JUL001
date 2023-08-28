/*You are part of a team developing a data analytics platform 
called "DataMetrics." As part of this platform, you have been 
assigned the task of creating a feature that allows users to 
read a CSV (Comma-Separated Values) file and calculate the 
average of a specific column. 
This feature will enable data analysts and business professionals 
to quickly analyze numerical data, gain insights, and make data-driven decisions.

To accomplish this, you decide to create a program that reads a CSV file and 
calculates the average of a specific column. The program will provide users with 
the average value, along with additional functionality to enhance their data analysis capabilities.

When a user opens the DataMetrics platform and accesses the data analytics section, 
they will be prompted to enter the path or name of the CSV file they want to analyze. 
The program will display a message like:

Welcome to DataMetrics Data Analytics!
Please enter the path or name of the CSV file:


The user can then input the path or name of the CSV file, for example: "sales_data.csv".

Upon receiving the input, the program will read the CSV file, extract the desired column data, 
and calculate the average. It will then display the result, saying:

Thank you for providing the CSV file.
The average value of the 'Sales' column is: $45,231.89
 */


const fs = require('fs');

function calculateColumnAverage(filePath, columnName) {
  const fileContent = fs.readFileSync(filePath, 'utf8');
  
  const rows = fileContent.split('\n');
  
  const headerRow = rows[0].split(',');
  
  const columnIndex = headerRow.findIndex((header) => header.trim().toLowerCase() === columnName.trim().toLowerCase());
  
  if (columnIndex === -1) {
    throw new Error(`Column "${columnName}" not found in the CSV.`);
  }
  
  const columnValues = rows.slice(1).map((row) => {
    const rowData = row.split(',');
    return rowData[columnIndex];
  });

  const numericValues = columnValues.map(Number).filter((value) => !isNaN(value));
  
  if (numericValues.length === 0) {
    throw new Error(`No numeric values found in the "${columnName}" column.`);
  }
  
  const sum = numericValues.reduce((acc, value) => acc + value, 0);
  const average = sum / numericValues.length;
  
  return average.toFixed(2);
}

function processCSVFile() {
  const filePath = prompt('Please enter the path or name of the CSV file:');
  const columnName = prompt('Please enter the name of the column to calculate its average:');
  
  if (filePath.trim() === '' || columnName.trim() === '') {
    console.log('No file path or column name provided.');
    return;
  }
  
  try {
    const average = calculateColumnAverage(filePath, columnName);
    
    console.log('Thank you for providing the CSV file.');
    console.log(`The average value of the '${columnName}' column is: $${average}`);
  } catch (error) {
    console.log('An error occurred:');
    console.log(error.message);
  }
}

processCSVFile();