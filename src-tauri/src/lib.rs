use std::{collections::HashMap, fmt::Debug};

use serde::{Deserialize, Serialize};
use serde_json::{from_value, Value};
use Algorithms::{
    divide_and_conquer::{binary_search, closest_pair},
    graph_algorithms::{bellman_ford, bfs, dfs, dijkstra},
    greedy_algorithms::{
        activity_selection, build_tree, fractional_knapsack::fractional_knapsack, generate_codes,
        kruskals_algorithm::kruskal, prim, Activity, Item,
    },
    sorting_algorithms::{
        bubble_sort, bucket_sort, heap_sort, insertion_sort, merge_sort, quick_sort,
        quick_sort_3way, radix_sort, selection_sort,
    },
};

pub mod Algorithms;

// Trait to support generic conversion from JSON arrays
pub trait FromJsonValue: Sized {
    fn from_json_value(v: &Value) -> Option<Self>;
}

impl FromJsonValue for i32 {
    fn from_json_value(v: &Value) -> Option<Self> {
        v.as_i64().map(|n| n as i32)
    }
}

impl FromJsonValue for f64 {
    fn from_json_value(v: &Value) -> Option<Self> {
        v.as_f64()
    }
}

impl FromJsonValue for String {
    fn from_json_value(v: &Value) -> Option<Self> {
        v.as_str().map(|s| s.to_string())
    }
}

pub fn convert_json_to_vec<T: FromJsonValue>(val: &Value) -> Option<Vec<T>> {
    val.as_array()?.iter().map(T::from_json_value).collect()
}

macro_rules! dispatch_sort {
    ($json:expr, $algo:expr,
        $($ty:ty => {
            $($name:literal => $func:expr),*
        }),*
    ) => {{
        let ty = $json.get("type").and_then(|v| v.as_str()).ok_or("Missing 'type'")?;
        match ty {
            $(
                stringify!($ty) => {
                    let arr_val = $json.get("arr").ok_or("Missing 'arr' field")?;
                    let mut arr = convert_json_to_vec::<$ty>(arr_val).ok_or("Failed to parse array")?;
                    match $algo {
                        $(
                            $name => {
                                $func(&mut arr);
                                Ok(format!("{:?}", arr))
                            },
                        )*
                        _ => Err("Unknown sorting algorithm".to_string()),
                    }
                },
            )*
            _ => Err("Unsupported type".to_string()),
        }
    }};
}

fn convert_json_to_vec_i32(json_val: &Value) -> Option<Vec<i32>> {
    if let Some(json_array) = json_val.as_array() {
        let mut result_vec = Vec::new();
        for item in json_array {
            if let Some(num_i64) = item.as_i64() {
                // JSON numbers are often parsed as i64 or f64
                // Convert i64 to i32, checking for potential overflow
                if num_i64 >= i32::MIN as i64 && num_i64 <= i32::MAX as i64 {
                    result_vec.push(num_i64 as i32);
                } else {
                    eprintln!("Number {} is out of i32 range.", num_i64);
                    return None; // Or handle error as appropriate
                }
            } else {
                eprintln!("Non-numeric value found in JSON array: {:?}", item);
                return None; // Or handle error
            }
        }
        Some(result_vec)
    } else {
        eprintln!("JSON value is not an array: {:?}", json_val);
        None // Not an array
    }
}
// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
fn my_custom_command(invoke_message: String) {
    println!("I was invoked from JavaScript! {}", invoke_message);
}

#[derive(Debug, Deserialize)]
pub struct InputDataFK {
    capacity: f64,
    items: Vec<Item>,
}

#[derive(Deserialize)]
struct InputKruskal {
    num_vertices: usize,
    edges: Vec<Algorithms::greedy_algorithms::kruskals_algorithm::Edge>,
}

#[tauri::command]
fn execute_json(json_data: serde_json::Value, selected_algo: String) -> Result<String, String> {
    println!("Received JSON: {:?}", json_data);

    match selected_algo.as_str() {
        "bubble sort"
        | "bucket sort"
        | "heap sort"
        | "insertion sort"
        | "merge sort"
        | "quick sort 3 partition"
        | "quick sort"
        | "selection sort" => dispatch_sort!(
            json_data,
            selected_algo.as_str(),
            i32 => {
                "bubble sort" => bubble_sort::<i32>,
                "bucket sort" => bucket_sort::<i32>,
                "heap sort" => heap_sort::<i32>,
                "insertion sort" => insertion_sort::<i32>,
                "merge sort" => merge_sort::<i32>,
                "quick sort 3 partition" => quick_sort_3way::<i32>,
                "quick sort" => quick_sort::<i32>,
                "selection sort" => selection_sort::<i32>
            },
            f64 => {
                "bubble sort" => bubble_sort::<f64>,
                "bucket sort" => bucket_sort::<f64>,
                "heap sort" => heap_sort::<f64>,
                "insertion sort" => insertion_sort::<f64>,
                "merge sort" => merge_sort::<f64>,
                "quick sort 3 partition" => quick_sort_3way::<f64>,
                "quick sort" => quick_sort::<f64>,
                "selection sort" => selection_sort::<f64>
            },
            String => {
                "bubble sort" => bubble_sort::<String>,
                "bucket sort" => bucket_sort::<String>,
                "heap sort" => heap_sort::<String>,
                "insertion sort" => insertion_sort::<String>,
                "merge sort" => merge_sort::<String>,
                "quick sort 3 partition" => quick_sort_3way::<String>,
                "quick sort" => quick_sort::<String>,
                "selection sort" => selection_sort::<String>
            }
        ),
        "radix sort" => {
            let arr_val = json_data
                .get("arr")
                .ok_or("Missing or invalid 'arr' field")?;
            let arr = convert_json_to_vec::<i32>(arr_val)
                .ok_or("Failed to parse array for radix sort")?;

            // Filter out negative values
            let mut arr: Vec<i32> = arr.into_iter().filter(|&x| x >= 0).collect();

            radix_sort(&mut arr);

            Ok(format!("{:?}", arr))
        }
        "fractional knapsack" => {
            let input: InputDataFK =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;
            let result = fractional_knapsack(input.items, input.capacity);
            Ok(format!("{:?}", result))
        }

        "huffman coding" => {
            let freq_map: HashMap<String, usize> =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;
            let converted: HashMap<char, usize> = freq_map
                .into_iter()
                .filter_map(|(k, v)| k.chars().next().map(|ch| (ch, v)))
                .collect();

            if let Some(tree) = build_tree(&converted) {
                let mut codes = HashMap::new();
                generate_codes(&tree, String::new(), &mut codes);
                Ok(format!("Huffman Codes: {:?}", codes))
            } else {
                Err("Huffman Failed".into())
            }
        }

        "kruskals algorithm" => {
            let input: InputKruskal =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;
            let mst = kruskal(input.num_vertices, input.edges);
            Ok(format!("{:?}", mst))
        }
        "prims algorithm" => {
            #[derive(Deserialize)]
            struct InputPrim {
                num_vertices: usize,
                edges: Vec<Algorithms::greedy_algorithms::prims_algorithm::Edge>,
            }

            let input: InputPrim =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;
            let mst = prim(input.num_vertices, input.edges);
            Ok(format!("{:?}", mst))
        }
        "bellman ford" => {
            #[derive(serde::Deserialize)]
            struct InputBellmanFord {
                vertex_count: usize,
                start: usize,
                edges: Vec<Algorithms::graph_algorithms::bellman_ford::Edge>,
            }

            let input: InputBellmanFord =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;

            match bellman_ford(&input.edges, input.vertex_count, input.start) {
                Ok(distances) => Ok(format!("{:?}", distances)),
                Err(e) => Err(e.into()),
            }
        }
        "breadth first search" => {
            #[derive(serde::Deserialize)]
            struct InputBFS {
                graph: Vec<Vec<usize>>,
                start: usize,
            }

            let input: InputBFS =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;

            let order = bfs(&input.graph, input.start);
            Ok(format!("{:?}", order))
        }
        "depth first search" => {
            #[derive(serde::Deserialize)]
            struct InputDFS {
                graph: Vec<Vec<usize>>,
                start: usize,
            }

            let input: InputDFS =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;

            let mut visited = vec![false; input.graph.len()];
            let mut order = Vec::new();

            dfs(&input.graph, input.start, &mut visited, &mut order);
            Ok(format!("{:?}", order))
        }
        "dijkstras algorithm" => {
            #[derive(serde::Deserialize)]
            struct InputDijkstra {
                adj_list: Vec<Vec<Algorithms::graph_algorithms::dijkstras_algorithm::Edge>>,
                start: usize,
            }

            let input: InputDijkstra =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;

            // Convert input edges to your Edge struct (if different, here they're the same)
            let adj_list: Vec<Vec<Algorithms::graph_algorithms::dijkstras_algorithm::Edge>> = input
                .adj_list
                .into_iter()
                .map(|vec_edge_input| {
                    vec_edge_input
                        .into_iter()
                        .map(
                            |e| Algorithms::graph_algorithms::dijkstras_algorithm::Edge {
                                node: e.node,
                                cost: e.cost,
                            },
                        )
                        .collect()
                })
                .collect();

            let dist = dijkstra(&adj_list, input.start);
            Ok(format!("{:?}", dist))
        }
        "activity selection" => {
            let mut activities: Vec<Activity> =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;
            let selected = activity_selection(&mut activities);
            Ok(format!("{:?}", selected))
        }
        "binary search" => {
            #[derive(serde::Deserialize)]
            struct InputType {
                #[serde(rename = "type")]
                typ: String,
            }

            // First, extract the "type" field only
            let input_type: InputType =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;

            match input_type.typ.as_str() {
                "i32" => {
                    #[derive(serde::Deserialize)]
                    struct InputBS {
                        arr: Vec<i32>,
                        target: i32,
                    }
                    let input: InputBS =
                        serde_json::from_value(json_data).map_err(|_| "Invalid JSON")?;
                    let result = binary_search(&input.arr, &input.target)
                        .map(|idx| idx as i32)
                        .unwrap_or(-1);
                    Ok(format!("{}", result))
                }
                "f64" => {
                    #[derive(serde::Deserialize)]
                    struct InputBS {
                        arr: Vec<f64>,
                        target: f64,
                    }
                    let input: InputBS =
                        serde_json::from_value(json_data).map_err(|_| "Invalid JSON")?;
                    let result = binary_search(&input.arr, &input.target)
                        .map(|idx| idx as i32)
                        .unwrap_or(-1);
                    Ok(format!("{}", result))
                }
                "string" | "String" => {
                    #[derive(serde::Deserialize)]
                    struct InputBS {
                        arr: Vec<String>,
                        target: String,
                    }
                    let input: InputBS =
                        serde_json::from_value(json_data).map_err(|_| "Invalid JSON")?;
                    let result = binary_search(&input.arr, &input.target)
                        .map(|idx| idx as i32)
                        .unwrap_or(-1);
                    Ok(format!("{}", result))
                }
                other => Err(format!("Unsupported type: {}", other).into()),
            }
        }

        "closest pair of points" => {
            let points: Vec<Algorithms::divide_and_conquer::closest_pair_of_points::Point> =
                serde_json::from_value(json_data.clone()).map_err(|_| "Invalid JSON")?;

            match closest_pair(&points) {
                Some((p1, p2, dist)) => Ok(format!(
                    "Closest points: ({:?}), ({:?}), Distance: {:.6}",
                    p1, p2, dist
                )),
                None => Err("Need at least two points".into()),
            }
        }
        _ => return Err("Wrong Algorithm Selected".into()),
    }
}

pub fn sort_pass<T: FromJsonValue + PartialOrd + Debug>(
    json_data: Value,
    sort: &str,
) -> Result<String, String> {
    if let Some(arr_val) = json_data.get("arr") {
        let mut arr =
            convert_json_to_vec::<T>(arr_val).ok_or("Failed to convert JSON array to vector")?;
        match sort {
            "bubble sort" => bubble_sort(&mut arr),
            // "bucket sort" => bucket_sort(&mut arr),
            // "heap sort" => heap_sort(&mut arr),
            // "insertion sort" => insertion_sort(&mut arr),
            // "merge sort" => merge_sort(&mut arr),
            // "quick sort 3 partition" => quick_sort_3way(&mut arr),
            // "quick sort" => quick_sort(&mut arr),
            // "radix sort" => radix_sort(&mut arr),
            // "selection sort" => selection_sort(&mut arr),
            _ => return Err("Wrong Algorithm Selected".into()),
        }

        Ok(format!("{:?}", arr))
    } else {
        Err("Missing 'arr' field in JSON".into())
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            greet,
            my_custom_command,
            execute_json
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
