import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def brute_force(points):
    """Find the smallest distance between points using brute force."""
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

def closest_in_strip(strip, d):
    """Find the closest pair of points in the strip."""
    min_dist = d
    strip.sort(key=lambda p: p.y)  # Sort by y-coordinate
    n = len(strip)
    for i in range(n):
        for j in range(i + 1, n):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist

def closest_pair_recursive(points_sorted_x, points_sorted_y):
    """Recursive function to find the closest pair of points."""
    n = len(points_sorted_x)
    if n <= 3:
        return brute_force(points_sorted_x)

    mid = n // 2
    mid_point = points_sorted_x[mid]

    left_x = points_sorted_x[:mid]
    right_x = points_sorted_x[mid:]
    left_y = list(filter(lambda p: p.x <= mid_point.x, points_sorted_y))
    right_y = list(filter(lambda p: p.x > mid_point.x, points_sorted_y))

    d_left = closest_pair_recursive(left_x, left_y)
    d_right = closest_pair_recursive(right_x, right_y)
    d = min(d_left, d_right)

    strip = [p for p in points_sorted_y if abs(p.x - mid_point.x) < d]
    return min(d, closest_in_strip(strip, d))

def closest_pair_of_points(points):
    """Main function to find the closest pair of points."""
    points_sorted_x = sorted(points, key=lambda p: p.x)
    points_sorted_y = sorted(points, key=lambda p: p.y)
    return closest_pair_recursive(points_sorted_x, points_sorted_y)

# Example usage
if __name__ == "__main__":
    points = [
        Point(2, 3),
        Point(12, 30),
        Point(40, 50),
        Point(5, 1),
        Point(12, 10),
        Point(3, 4)
    ]
    result = closest_pair_of_points(points)
    print(f"The smallest distance is: {result}")