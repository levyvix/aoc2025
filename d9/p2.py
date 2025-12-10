from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

content = open(0).read()
red_tiles = [tuple(map(int, line.split(","))) for line in content.splitlines()]

# Create line segments from consecutive red tiles
# Each line is represented as (x_min, x_max, y_min, y_max)
lines = []
for i in range(len(red_tiles)):
    x1, y1 = red_tiles[i]
    x2, y2 = red_tiles[(i + 1) % len(red_tiles)]
    # Store as bounding box of the line segment
    lines.append((min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)))

# Function to check if two rectangles overlap
def rectangles_overlap(r1, r2):
    """Check if two axis-aligned rectangles overlap (including touching edges)"""
    x1_min, x1_max, y1_min, y1_max = r1
    x2_min, x2_max, y2_min, y2_max = r2
    # They DON'T overlap if one is completely to the left/right/above/below the other
    return not (x1_max < x2_min or x2_max < x1_min or y1_max < y2_min or y2_max < y1_min)

# Function to check if rectangle is valid
def check_rectangle_valid(x1, x2, y1, y2):
    """Check if rectangle is valid

    A rectangle is valid if its inner area (shrunk by 1 on all sides)
    does NOT overlap with any boundary lines.
    """
    # Get rectangle bounds
    rect_min_x = min(x1, x2)
    rect_max_x = max(x1, x2)
    rect_min_y = min(y1, y2)
    rect_max_y = max(y1, y2)

    # Shrink by 1 on all sides to get inner rectangle
    inner_x_min = rect_min_x + 1
    inner_x_max = rect_max_x - 1
    inner_y_min = rect_min_y + 1
    inner_y_max = rect_max_y - 1

    # If inner rectangle is invalid, the rectangle is too small to be valid
    if inner_x_min > inner_x_max or inner_y_min > inner_y_max:
        return False

    inner_rect = (inner_x_min, inner_x_max, inner_y_min, inner_y_max)

    # Check if inner area overlaps with any boundary line
    for line in lines:
        if rectangles_overlap(inner_rect, line):
            return False

    # No overlaps with any boundary line - rectangle is valid!
    return True

# Generate all rectangles
rectangles = []
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[j]

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        rectangles.append((area, x1, x2, y1, y2))

# Sort by area descending to check largest first
rectangles.sort(reverse=True)

# Find the largest valid rectangle
ans = 0
for area, x1, x2, y1, y2 in rectangles:
    # Skip if smaller than current best
    if area <= ans:
        break

    # Check if this rectangle is valid
    if check_rectangle_valid(x1, x2, y1, y2):
        ans = area
        break

ic(ans)
