def quick_sort(arr):
    """
    Perform quick sort on an array.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    # Choose the pivot (here we use the last element)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Recursively sort left and right partitions and combine with pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

