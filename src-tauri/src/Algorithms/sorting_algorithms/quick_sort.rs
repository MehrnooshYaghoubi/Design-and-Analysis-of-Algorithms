pub fn quick_sort<T: PartialOrd + Clone>(arr: &mut [T]) {
    if arr.len() < 2 {
        return;
    }
    quick_sort_recursive(arr, 0, arr.len() - 1);
}

fn quick_sort_recursive<T: PartialOrd + Clone>(arr: &mut [T], low: usize, high: usize) {
    if low < high {
        let pivot_index = partition(arr, low, high);
        if pivot_index > 0 {
            quick_sort_recursive(arr, low, pivot_index - 1);
        }
        quick_sort_recursive(arr, pivot_index + 1, high);
    }
}

fn partition<T: PartialOrd + Clone>(arr: &mut [T], low: usize, high: usize) -> usize {
    let pivot = arr[high].clone();
    let mut i = low;

    for j in low..high {
        // Use partial_cmp and treat None as Greater to skip NaNs or undefined comparisons
        if arr[j]
            .partial_cmp(&pivot)
            .unwrap_or(std::cmp::Ordering::Greater)
            != std::cmp::Ordering::Greater
        {
            arr.swap(i, j);
            i += 1;
        }
    }

    arr.swap(i, high);
    i
}
