"""
You are part of a team developing a search engine called "Searchify."
As part of this search engine, you have been assigned the task of creating a feature that implements
a binary search algorithm to efficiently find a specific element in a sorted list of data.
This feature will assist users in searching for specific information, retrieving relevant results quickly,
and improving the overall search experience. To accomplish this,
you decide to create a program that takes a sorted list of elements as input and
implements the binary search algorithm to find a specific element.
The program will provide users with the search result,
along with additional functionality to enhance their search capabilities.
"""


def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if sorted_list[mid] == target:
            return mid  # Element found, return index
        elif sorted_list[mid] < target:
            left = mid + 1  # Adjust left boundary
        else:
            right = mid - 1  # Adjust right boundary

    return -1  # Element not found


def main():
    sorted_list = [100, 20, 30, 40, 50, 60, 70, 80, 90]

    target = 40

    index = binary_search(sorted_list, target)

    print(sorted_list)
    if index != -1:
        print(f"The element {target} was found at index {index}.")
    else:
        print(f"The element {target} was not found in the list.")


if __name__ == "__main__":
    main()
