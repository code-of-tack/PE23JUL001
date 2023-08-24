/* You are part of a team developing an e-commerce platform called "ShopSmart." As part of this platform, 
you have been assigned the task of creating a feature that helps users find the second-largest price among a list
 of products. This feature will assist users in making informed purchasing decisions, comparing prices,
 and identifying the best deals available. */

 // Function to find the second-largest price from a list of products
function findSecondLargestPrice(prices) {
    if (prices.length < 2) {
      throw new Error('At least two prices are required.');
    }
  
    let maxPrice = -Infinity;
    let secondMaxPrice = -Infinity;
  
    // Iterate through each price
    for (let i = 0; i < prices.length; i++) {
      const price = prices[i];
  
      if (price > maxPrice) {
        // If the current price is greater than the max price,
        // update both maxPrice and secondMaxPrice accordingly
        secondMaxPrice = maxPrice;
        maxPrice = price;
      } else if (price > secondMaxPrice && price < maxPrice) {
        // If the current price is greater than the second max price
        // and less than the max price, update only secondMaxPrice
        secondMaxPrice = price;
      }
    }
  
    // Return the second-largest price
    return secondMaxPrice;
  }
  
  // Function to handle user input and display the result
  function productBrowsing() {
    console.log("Welcome to ShopSmart Product Browsing!");
    console.log("Here are the prices of the available products:");
    const prices = [9.99, 14.99, 24.99, 19.99, 12.99, 29.99, 8.99]; 
  
    // Call the findSecondLargestPrice function to find the second-largest price
    try {
      const result = findSecondLargestPrice(prices);
  
      // Display the result
      console.log("The second-largest price among the products is: $" + result.toFixed(2));
    } catch (error) {
      console.log(error.message);
    }
  }
  
  // Call the productBrowsing function to start the product browsing tool
  productBrowsing();