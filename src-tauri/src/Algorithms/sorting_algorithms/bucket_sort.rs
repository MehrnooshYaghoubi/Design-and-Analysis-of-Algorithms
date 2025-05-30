pub fn bucket_sort(arr: &mut Vec<i32>) {
    let n = arr.len();
    if n == 0 {
        return;
    }

    // Determine the maximum value to normalize the integers
    // If you know the max value beforehand, you can use that instead.
    let max_val = *arr.iter().max().unwrap_or(&0);
    if max_val == 0 {
        // Handle case where all elements are 0
        return;
    }

    // Create n empty buckets
    let mut buckets: Vec<Vec<i32>> = vec![Vec::new(); n];

    // Put array elements into different buckets
    for &value in arr.iter() {
        // Normalize the integer to a f64 between 0.0 and less than 1.0
        let normalized_value = value as f64 / (max_val as f64 + 1.0);
        let mut index = (normalized_value * n as f64) as usize;
        // Ensure index is within bounds (0 to n-1)
        if index >= n {
            index = n - 1;
        }
        buckets[index].push(value);
    }

    // Sort individual buckets
    for bucket in buckets.iter_mut() {
        bucket.sort(); // sort for i32
    }

    // Concatenate all buckets into arr
    let mut i = 0;
    for bucket in buckets {
        for value in bucket {
            arr[i] = value;
            i += 1;
        }
    }
}
