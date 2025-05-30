use std::cmp::Ordering;
use std::f64;

use serde::Deserialize;

#[derive(Debug, Clone, Copy)]
pub struct Point {
    pub x: f64,
    pub y: f64,
}

impl Point {
    fn distance(&self, other: &Point) -> f64 {
        (self.x - other.x).powi(2) + ((self.y - other.y).powi(2)).sqrt()
    }
}

pub fn closest_pair(points: &[Point]) -> (Point, Point, f64) {
    let mut points_sorted_x = points.to_vec();
    points_sorted_x.sort_by(|a, b| a.x.partial_cmp(&b.x).unwrap());

    closest_pair_recursive(&points_sorted_x)
}

fn closest_pair_recursive(points: &[Point]) -> (Point, Point, f64) {
    let n = points.len();
    if n <= 3 {
        return brute_force_closest_pair(points);
    }

    let mid = n / 2;
    let mid_point = points[mid];

    let (left_pair, left_dist) = {
        let (p1, p2, d) = closest_pair_recursive(&points[..mid]);
        (p1, p2, d)
    };

    let (right_pair, right_dist) = {
        let (p1, p2, d) = closest_pair_recursive(&points[mid..]);
        (p1, p2, d)
    };

    let (mut min_pair, mut min_dist) = if left_dist < right_dist {
        (left_pair, left_dist)
    } else {
        (right_pair, right_dist)
    };

    let strip: Vec<Point> = points
        .iter()
        .filter(|p| (p.x - mid_point.x).abs() < min_dist)
        .cloned()
        .collect();

    let (strip_pair, strip_dist) = closest_pair_in_strip(&strip, min_dist);
    if strip_dist < min_dist {
        min_pair = strip_pair;
        min_dist = strip_dist;
    }

    (min_pair.0, min_pair.1, min_dist)
}

fn brute_force_closest_pair(points: &[Point]) -> (Point, Point, f64) {
    let mut min_dist = f64::INFINITY;
    let mut pair = (points[0], points[1]);

    for i in 0..points.len() {
        for j in i + 1..points.len() {
            let dist = points[i].distance(&points[j]);
            if dist < min_dist {
                min_dist = dist;
                pair = (points[i], points[j]);
            }
        }
    }

    (pair.0, pair.1, min_dist)
}

fn closest_pair_in_strip(strip: &[Point], min_dist: f64) -> ((Point, Point), f64) {
    let mut min_dist = min_dist;
    let mut min_pair = (strip[0], strip[1]);
    let n = strip.len();

    strip.sort_by(|a, b| a.y.partial_cmp(&b.y).unwrap());

    for i in 0..n {
        let mut j = i + 1;
        while j < n && (strip[j].y - strip[i].y) < min_dist {
            let dist = strip[i].distance(&strip[j]);
            if dist < min_dist {
                min_dist = dist;
                min_pair = (strip[i], strip[j]);
            }
            j += 1;
        }
    }

    (min_pair, min_dist)
}
