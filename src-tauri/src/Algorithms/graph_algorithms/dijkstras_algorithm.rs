use std::cmp::Ordering;
use std::collections::BinaryHeap;

use serde::Deserialize;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: usize,
    position: usize,
}

// The priority queue depends on `Ord`. We want smallest cost first,
// so we implement `Ord` accordingly.
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        // Notice that the we flip the order here
        other
            .cost
            .cmp(&self.cost)
            .then_with(|| self.position.cmp(&other.position))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// Each edge has a target node and a cost (weight)
#[derive(Copy, Clone, Deserialize)]
pub struct Edge {
    pub node: usize,
    pub cost: usize,
}

pub fn dijkstra(adj_list: &Vec<Vec<Edge>>, start: usize) -> Vec<usize> {
    let n = adj_list.len();
    let mut dist = vec![usize::MAX; n];
    let mut heap = BinaryHeap::new();

    dist[start] = 0;
    heap.push(State {
        cost: 0,
        position: start,
    });

    while let Some(State { cost, position }) = heap.pop() {
        // If we already found a better way, skip
        if cost > dist[position] {
            continue;
        }

        // Relax edges
        for edge in &adj_list[position] {
            let next = State {
                cost: cost + edge.cost,
                position: edge.node,
            };

            if next.cost < dist[next.position] {
                dist[next.position] = next.cost;
                heap.push(next);
            }
        }
    }

    dist
}

fn main() {
    // Example graph: adjacency list
    // Each vector at index i contains edges from node i
    let graph = vec![
        vec![Edge { node: 1, cost: 4 }, Edge { node: 2, cost: 1 }],
        vec![Edge { node: 3, cost: 1 }],
        vec![Edge { node: 1, cost: 2 }, Edge { node: 3, cost: 5 }],
        vec![],
    ];

    let start_node = 0;
    let distances = dijkstra(&graph, start_node);

    for (i, d) in distances.iter().enumerate() {
        println!("Distance from node {} to node {} is {}", start_node, i, d);
    }
}
