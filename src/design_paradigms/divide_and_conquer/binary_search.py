def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.

    Parameters:
        arr (list): A sorted list of elements.
        target (int): The element to search for.

    Returns:
        int: The index of the target element in the array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow for large indices
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

