"""
You are part of a team developing a music streaming platform called "SoundWave." As part of this platform,
you have been assigned the task of creating a feature that implements a merge sort algorithm
to efficiently sort a playlist of songs based on their popularity.
This feature will assist users in discovering popular songs, creating personalized playlists,
and enhancing their overall music streaming experience.
To accomplish this, you decide to create a program that takes a list of integers representing song popularity and
implements the merge sort algorithm to sort the songs in descending order of popularity.
The program will provide users with the sorted playlist,
along with additional functionality to enhance their music streaming capabilities.
"""


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    sorted_arr = []
    l_index, r_index = 0, 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] > right[r_index]:
            sorted_arr.append(left[l_index])
            l_index += 1
        else:
            sorted_arr.append(right[r_index])
            r_index += 1

    sorted_arr.extend(left[l_index:])
    sorted_arr.extend(right[r_index:])

    return sorted_arr


def main():
    print("Welcome to SoundWave - Top Songs!")

    # Input unsorted playlist as a list of integers
    unsorted_playlist = [int(x) for x in
                         input("Enter the unsorted playlist of song popularities separated by commas: ").split(',')]

    # Apply merge sort to sort the playlist in descending order of popularity
    sorted_playlist = merge_sort(unsorted_playlist)

    print("\nThank you for using SoundWave - Top Songs!")
    print("Here is your sorted playlist in descending order of popularity:")
    print(", ".join(map(str, sorted_playlist)))


if __name__ == '__main__':
    main()
