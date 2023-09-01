/* You are part of a team developing a social networking platform called "SocialGraph." As part of this platform, 
you have been assigned the task of creating a feature that implements a depth-first search (DFS) algorithm to traverse 
the user graph. This feature will assist users in discovering connections, exploring networks of friends,
 and identifying mutual friends within the platform. */

 // Class representing a user in the graph
class User {
    constructor(id) {
      this.id = id;
      this.friends = [];
    }
  
    addFriend(user) {
      this.friends.push(user);
      user.friends.push(this);
    }
  }
  
  // Function to perform DFS traversal on the user graph
  function dfsTraversal(startUser) {
    const visited = new Set();
    const traversalResult = [];
  
    function dfs(user) {
      visited.add(user);
      traversalResult.push(user.id);
  
      for (const friend of user.friends) {
        if (!visited.has(friend)) {
          dfs(friend);
        }
      }
    }
  
    dfs(startUser);
  
    return traversalResult;
  }
  // Function to handle user input and display the DFS traversal result
  function main() {
    console.log("Welcome to SocialGraph - Explore Connections!");
    console.log("Please enter the starting user ID for DFS traversal:");
  
    // Create the user graph (replace this with your own graph creation logic)
    const user1 = new User(12345);
    const user2 = new User(56789);
    const user3 = new User(98765);
    const user4 = new User(43210);
  
    user1.addFriend(user2);
    user1.addFriend(user3);
    user2.addFriend(user4);
  
    // Read user input from the command line or any other input mechanism
    const startUserId = 12345; // Replace this line with the actual user ID input
  
    // Find the start user in the graph
    let startUser = null;
    if (startUserId === user1.id) {
      startUser = user1;
    } else if (startUserId === user2.id) {
      startUser = user2;
    } else if (startUserId === user3.id) {
      startUser = user3;
    } else if (startUserId === user4.id) {
      startUser = user4;
    }
  
    // Perform DFS traversal on the user graph
    const traversalResult = dfsTraversal(startUser);
  
    // Display the DFS traversal result
    console.log("Thank you for providing the starting user ID.");
    console.log("DFS traversal result:");
    console.log(traversalResult.join(" -> "));
  }
  
  // Call the main function to start the Explore Connections feature
  main();