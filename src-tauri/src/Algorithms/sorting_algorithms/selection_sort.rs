pub fn selection_sort<T: PartialOrd + Clone>(collection: &mut Vec<T>) {
    let length = collection.len();

    for i in 0..length.saturating_sub(1) {
        let mut least = i;
        for k in (i + 1)..length {
            if let Some(true) = collection[k]
                .partial_cmp(&collection[least])
                .map(|o| o.is_lt())
            {
                least = k;
            }
        }
        collection.swap(i, least);
    }
}
