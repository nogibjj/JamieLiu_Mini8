# main.py


def merge_sort(arr):
    """
    Perform merge sort on the given array.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A sorted version of the input list.
    """
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    left (list): The left half.
    right (list): The right half.

    Returns:
    list: Merged and sorted list.
    """
    sorted_list = []
    i = j = 0

    # Merge the lists while comparing elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


if __name__ == "__main__":
    # Example usage
    example_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", example_array)
    sorted_array = merge_sort(example_array)
    print("Sorted array:", sorted_array)
