use std::collections::VecDeque;

pub fn bfs(graph: &Vec<Vec<usize>>, start: usize) -> Vec<usize> {
    let mut visited = vec![false; graph.len()];
    let mut queue = VecDeque::new();
    let mut order = Vec::new();

    visited[start] = true;
    queue.push_back(start);

    while let Some(node) = queue.pop_front() {
        order.push(node);

        for &neighbor in &graph[node] {
            if !visited[neighbor] {
                visited[neighbor] = true;
                queue.push_back(neighbor);
            }
        }
    }

    order
}

fn main() {
    let graph = vec![vec![1, 2], vec![2], vec![0, 3], vec![3]];

    let start = 2;
    let bfs_order = bfs(&graph, start);

    println!("BFS starting from node {}: {:?}", start, bfs_order);
}
