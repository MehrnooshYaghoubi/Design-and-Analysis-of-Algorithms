use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize, Clone)]
pub struct Activity {
    start: usize,
    finish: usize,
}

pub fn activity_selection(activities: &mut [Activity]) -> Vec<Activity> {
    activities.sort_by_key(|a| a.finish);

    let mut selected = Vec::new();
    let mut last_finish_time = 0;

    for activity in activities.iter() {
        if activity.start >= last_finish_time {
            selected.push(activity.clone());
            last_finish_time = activity.finish;
        }
    }

    selected
}

fn main() {
    let mut activities = vec![
        Activity {
            start: 1,
            finish: 4,
        },
        Activity {
            start: 3,
            finish: 5,
        },
        Activity {
            start: 0,
            finish: 6,
        },
        Activity {
            start: 5,
            finish: 7,
        },
        Activity {
            start: 3,
            finish: 9,
        },
        Activity {
            start: 5,
            finish: 9,
        },
        Activity {
            start: 6,
            finish: 10,
        },
        Activity {
            start: 8,
            finish: 11,
        },
        Activity {
            start: 8,
            finish: 12,
        },
        Activity {
            start: 2,
            finish: 14,
        },
        Activity {
            start: 12,
            finish: 16,
        },
    ];

    let selected = activity_selection(&mut activities);

    println!("Selected activities:");
    for activity in selected {
        println!("Start: {}, Finish: {}", activity.start, activity.finish);
    }
}
