"""
You are part of a team developing an e-commerce platform called "MarketPro." As part of this platform,
you have been assigned the task of creating a feature that finds the kth largest element in an unsorted list.
This feature will assist users in identifying popular products, analyzing sales trends,
and optimizing their purchasing decisions. To accomplish this,
you decide to create a program that takes an unsorted list of elements and finds the kth largest element.
The program will provide users with the result,
along with additional functionality to enhance their shopping experience.
"""


def find_kth_largest(nums, k):

    nums.sort(reverse=True)
    return nums[k - 1]

def main():
    print("Welcome to MarketPro - Popular Products!")
    k = int(input("Please enter the value of k to find the kth largest element: "))

    unsorted_list = [int(x) for x in input("Enter the unsorted list of elements separated by spaces: ").split()]

    kth_largest = find_kth_largest(unsorted_list, k)

    print("\nThank you for providing the value of k.")
    print("The kth largest element is:", kth_largest)


if __name__ == '__main__':
    main()
