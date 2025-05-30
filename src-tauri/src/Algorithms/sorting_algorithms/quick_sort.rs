pub fn quick_sort(arr: &mut Vec<i32>) {
    if arr.len() < 2 {
        return;
    }
    quick_sort_recursive(arr, 0, arr.len() - 1);
}

fn quick_sort_recursive(arr: &mut Vec<i32>, low: usize, high: usize) {
    if low < high {
        let pivot_index = partition(arr, low, high);
        if pivot_index > 0 {
            quick_sort_recursive(arr, low, pivot_index - 1);
        }
        quick_sort_recursive(arr, pivot_index + 1, high);
    }
}

fn partition(arr: &mut Vec<i32>, low: usize, high: usize) -> usize {
    let pivot = arr[high];
    let mut i = low;

    for j in low..high {
        if arr[j] <= pivot {
            arr.swap(i, j);
            i += 1;
        }
    }

    arr.swap(i, high);
    i
}
