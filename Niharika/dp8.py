def find_kth_largest(nums, k):
    # Use a sorting algorithm to sort the list in descending order
    nums.sort(reverse=True)
    
    # Return the kth largest element
    return nums[k - 1]

def main():
    print("Welcome to MarketPro - Popular Products!")
    nums = input("Please enter a list of numbers separated by spaces: ").split()
    nums = [int(num) for num in nums]  # Convert input to a list of integers
    k = int(input("Please enter the value of k to find the kth largest element: "))
    
    if k < 1 or k > len(nums):
        print("Invalid value of k. Please enter a valid value.")
        return
    
    kth_largest = find_kth_largest(nums, k)
    print("Thank you for providing the value of k.")
    print(f"The kth largest element is: {kth_largest}")

if __name__ == "__main__":
    main()
    