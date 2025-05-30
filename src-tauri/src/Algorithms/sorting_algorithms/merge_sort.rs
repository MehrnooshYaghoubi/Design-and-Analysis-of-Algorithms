pub fn merge_sort(arr: &mut Vec<i32>) {
    // Base case: if the vector has 0 or 1 element, it's already sorted
    if arr.len() <= 1 {
        return;
    }

    let mid = arr.len() / 2;

    // Split the vector into two halves.
    // We create new Vecs for left and right for simplicity in this recursive approach.
    // For a more in-place merge sort, a different approach with indices is needed.
    let mut left_half = arr[..mid].to_vec();
    let mut right_half = arr[mid..].to_vec();

    // Recursively sort the two halves
    merge_sort(&mut left_half);
    merge_sort(&mut right_half);

    // Merge the sorted halves back into the original array
    merge_i32(arr, &left_half, &right_half);
}

fn merge_i32(arr: &mut Vec<i32>, left: &Vec<i32>, right: &Vec<i32>) {
    let mut i = 0; // Pointer for the left array
    let mut j = 0; // Pointer for the right array
    let mut k = 0; // Pointer for the merged array (arr)

    // Compare elements from left and right and place them into arr in sorted order
    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            arr[k] = left[i]; // No .clone() needed for i32
            i += 1;
        } else {
            arr[k] = right[j]; // No .clone() needed for i32
            j += 1;
        }
        k += 1;
    }

    // Copy any remaining elements from the left array
    while i < left.len() {
        arr[k] = left[i]; // No .clone() needed for i32
        i += 1;
        k += 1;
    }

    // Copy any remaining elements from the right array
    while j < right.len() {
        arr[k] = right[j]; // No .clone() needed for i32
        j += 1;
        k += 1;
    }
}
