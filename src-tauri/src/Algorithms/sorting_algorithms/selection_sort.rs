pub fn selection_sort(collection: &mut Vec<i32>) {
    let length = collection.len();

    for i in 0..length.saturating_sub(1) {
        let mut least = i;
        for k in (i + 1)..length {
            if collection[k] < collection[least] {
                least = k;
            }
        }
        collection.swap(i, least);
    }
}
