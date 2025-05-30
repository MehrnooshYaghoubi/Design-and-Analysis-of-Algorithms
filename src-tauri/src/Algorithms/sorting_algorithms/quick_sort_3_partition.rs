pub fn quick_sort_3way(arr: &mut Vec<i32>) {
    let len = arr.len();
    if len <= 1 {
        return;
    }

    // Use a helper function that operates on a slice,
    // as it's more idiomatic for sorting sub-parts of a Vec
    // without reallocating or cloning.
    quick_sort_3way_slice(arr);
}

// Helper function to perform 3-way quicksort on a slice
fn quick_sort_3way_slice(arr_slice: &mut [i32]) {
    let len = arr_slice.len();
    if len <= 1 {
        return;
    }

    let mut lt = 0; // arr_slice[0..lt] < pivot
    let mut gt = len - 1; // arr_slice[gt+1..] > pivot
    let pivot = arr_slice[0]; // choose the first element as pivot
    let mut i = 1;

    while i <= gt {
        if arr_slice[i] < pivot {
            arr_slice.swap(lt, i);
            lt += 1;
            i += 1;
        } else if arr_slice[i] > pivot {
            arr_slice.swap(i, gt);
            // Handle the case where gt becomes 0, preventing underflow
            if gt == 0 {
                break;
            }
            gt -= 1;
        } else {
            i += 1;
        }
    }

    // Recursively sort the parts < pivot and > pivot
    // Note: These calls are on slices, which is efficient.
    quick_sort_3way_slice(&mut arr_slice[0..lt]);
    quick_sort_3way_slice(&mut arr_slice[gt + 1..]);
}
