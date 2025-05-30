use serde::Deserialize;

#[derive(Debug, Clone, Copy, Deserialize)]
pub struct Edge {
    pub from: usize,
    pub to: usize,
    pub weight: isize,
}

pub fn bellman_ford(
    edges: &[Edge],
    vertex_count: usize,
    start: usize,
) -> Result<Vec<isize>, &'static str> {
    let mut dist = vec![isize::MAX; vertex_count];
    dist[start] = 0;

    // Relax edges repeatedly
    for _ in 0..vertex_count - 1 {
        let mut updated = false;
        for edge in edges {
            if dist[edge.from] != isize::MAX && dist[edge.from] + edge.weight < dist[edge.to] {
                dist[edge.to] = dist[edge.from] + edge.weight;
                updated = true;
            }
        }
        if !updated {
            break;
        }
    }

    // Check for negative weight cycles
    for edge in edges {
        if dist[edge.from] != isize::MAX && dist[edge.from] + edge.weight < dist[edge.to] {
            return Err("Graph contains a negative weight cycle");
        }
    }

    Ok(dist)
}

fn main() {
    let edges = vec![
        Edge {
            from: 0,
            to: 1,
            weight: 6,
        },
        Edge {
            from: 0,
            to: 2,
            weight: 7,
        },
        Edge {
            from: 1,
            to: 2,
            weight: 8,
        },
        Edge {
            from: 1,
            to: 3,
            weight: 5,
        },
        Edge {
            from: 1,
            to: 4,
            weight: -4,
        },
        Edge {
            from: 2,
            to: 3,
            weight: -3,
        },
        Edge {
            from: 2,
            to: 4,
            weight: 9,
        },
        Edge {
            from: 3,
            to: 1,
            weight: -2,
        },
        Edge {
            from: 4,
            to: 0,
            weight: 2,
        },
        Edge {
            from: 4,
            to: 3,
            weight: 7,
        },
    ];

    let vertex_count = 5;
    let start_node = 0;

    match bellman_ford(&edges, vertex_count, start_node) {
        Ok(distances) => {
            for (i, dist) in distances.iter().enumerate() {
                println!(
                    "Distance from node {} to node {} is {}",
                    start_node, i, dist
                );
            }
        }
        Err(msg) => println!("Error: {}", msg),
    }
}
