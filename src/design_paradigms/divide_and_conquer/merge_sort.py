def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.

    Parameters:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A merged and sorted list.
    """
    sorted_array = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array
