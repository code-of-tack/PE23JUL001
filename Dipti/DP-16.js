/* You are part of a team developing a music streaming platform called "SoundWave." As part of this platform,
 you have been assigned the task of creating a feature that implements a merge sort algorithm to efficiently 
 sort a playlist of songs based on their popularity. This feature will assist users in discovering popular songs, 
 creating personalized playlists, and enhancing their overall music streaming experience. */

 // Merge two sorted arrays into a single sorted array
function merge(left, right) {
    let merged = [];
    let i = 0;
    let j = 0;
  
    while (i < left.length && j < right.length) {
      if (left[i] > right[j]) {
        merged.push(left[i]);
        i++;
      } else {
        merged.push(right[j]);
        j++;
      }
    }
  
    // Copy any remaining elements from left and right arrays
    while (i < left.length) {
      merged.push(left[i]);
      i++;
    }
  
    while (j < right.length) {
      merged.push(right[j]);
      j++;
    }
  
    return merged;
  }
  
  // Merge sort algorithm
  function mergeSort(arr) {
    if (arr.length <= 1) {
      return arr;
    }
  
    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);
  
    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);
  
    return merge(sortedLeft, sortedRight);
  }
    // Function to handle user input and display the sorted playlist
    function main() {
        console.log("Welcome to SoundWave - Top Songs!");
        console.log("Here is your unsorted playlist of song popularities:");
        console.log("78, 56, 90, 120, 45, 80, ...");
      
        // Create the unsorted playlist of song popularities (replace this with your own list)
        const playlist = [78, 56, 90, 120, 45, 80];
      
        // Apply merge sort to sort the playlist
        const sortedPlaylist = mergeSort(playlist);
      
        // Display the sorted playlist
        console.log("Thank you for using SoundWave - Top Songs!");
        console.log("Here is your sorted playlist in descending order of popularity:");
        console.log(sortedPlaylist.join(", "));
      }
      
      // Call the main function to start the Top Songs feature
      main();