pub fn dfs(graph: &Vec<Vec<usize>>, start: usize, visited: &mut Vec<bool>, order: &mut Vec<usize>) {
    visited[start] = true;
    order.push(start);

    for &neighbor in &graph[start] {
        if !visited[neighbor] {
            dfs(graph, neighbor, visited, order);
        }
    }
}

fn main() {
    let graph = vec![vec![1, 2], vec![2], vec![0, 3], vec![3]];

    let start = 2;
    let mut visited = vec![false; graph.len()];
    let mut dfs_order = Vec::new();

    dfs(&graph, start, &mut visited, &mut dfs_order);

    println!("DFS starting from node {}: {:?}", start, dfs_order);
}
