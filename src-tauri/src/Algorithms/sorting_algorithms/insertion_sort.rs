pub fn insertion_sort<T: PartialOrd + Clone>(arr: &mut Vec<T>) {
    let n = arr.len();

    for i in 1..n {
        let key = arr[i].clone();
        let mut j = i;
        while j > 0 && arr[j - 1] > key {
            arr[j] = arr[j - 1].clone();
            j -= 1;
        }
        arr[j] = key;
    }
}
