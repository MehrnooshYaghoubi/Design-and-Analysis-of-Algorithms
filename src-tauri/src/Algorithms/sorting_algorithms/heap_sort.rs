pub fn heap_sort(arr: &mut Vec<i32>) {
    let n = arr.len();

    // Build max heap
    for i in (0..n / 2).rev() {
        heapify(arr, n, i);
    }

    // Extract elements from heap one by one
    for i in (1..n).rev() {
        arr.swap(0, i); // Move current root to end
        heapify(arr, i, 0); // Heapify reduced heap
    }
}

fn heapify(arr: &mut Vec<i32>, heap_size: usize, root_index: usize) {
    let mut largest = root_index;
    let left = 2 * root_index + 1;
    let right = 2 * root_index + 2;

    if left < heap_size && arr[left] > arr[largest] {
        largest = left;
    }

    if right < heap_size && arr[right] > arr[largest] {
        largest = right;
    }

    if largest != root_index {
        arr.swap(root_index, largest);
        heapify(arr, heap_size, largest);
    }
}
