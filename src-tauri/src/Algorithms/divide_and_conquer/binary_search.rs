pub fn binary_search(arr: &[i32], target: i32) -> i32 {
    let mut left = 0;
    let mut right = arr.len() as i32 - 1;

    while left <= right {
        let mid = left + (right - left) / 2;
        let mid_val = arr[mid as usize];

        if mid_val == target {
            return mid;
        } else if mid_val < target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    -1 // Target not found
}
