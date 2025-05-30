use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

use serde::Deserialize;

#[derive(Debug, Clone, Deserialize)]
pub struct Edge {
    pub src: usize,
    pub dest: usize,
    pub weight: i32,
}

pub fn prim(n: usize, edges: Vec<Edge>) -> Vec<Edge> {
    // Build adjacency list from edge list
    let mut adj = vec![vec![]; n];
    for edge in edges {
        adj[edge.src].push((edge.dest, edge.weight));
        adj[edge.dest].push((edge.src, edge.weight)); // undirected graph
    }

    let mut mst = Vec::new();
    let mut visited = HashSet::new();
    let mut heap = BinaryHeap::new();

    visited.insert(0);
    for &(neighbor, weight) in &adj[0] {
        heap.push(Reverse((weight, 0, neighbor)));
    }

    while let Some(Reverse((weight, u, v))) = heap.pop() {
        if visited.contains(&v) {
            continue;
        }

        visited.insert(v);
        mst.push(Edge {
            src: u,
            dest: v,
            weight,
        });

        for &(neighbor, w) in &adj[v] {
            if !visited.contains(&neighbor) {
                heap.push(Reverse((w, v, neighbor)));
            }
        }
    }

    mst
}

fn main() {
    let n = 5;
    let edges = vec![
        Edge {
            src: 0,
            dest: 1,
            weight: 2,
        },
        Edge {
            src: 0,
            dest: 3,
            weight: 6,
        },
        Edge {
            src: 1,
            dest: 2,
            weight: 3,
        },
        Edge {
            src: 1,
            dest: 3,
            weight: 8,
        },
        Edge {
            src: 1,
            dest: 4,
            weight: 5,
        },
        Edge {
            src: 2,
            dest: 4,
            weight: 7,
        },
        Edge {
            src: 3,
            dest: 4,
            weight: 9,
        },
    ];

    let mst = prim(n, edges);

    println!("Edges in the MST (Prim's Algorithm):");
    for edge in mst {
        println!("{} -- {} == {}", edge.src, edge.dest, edge.weight);
    }
}
