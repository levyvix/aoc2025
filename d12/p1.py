import re
import sys
from datetime import datetime

current_datetime = datetime.now()
answerp1 = 0
closest_call = float('inf')
total_area_of_closest_call = None

# Read from stdin
input_text = sys.stdin.read().strip()
lines = input_text.split('\n')

# Auto-generate ranges: lines 1-3, 6-8, 11-13, etc.
# Count # in each shape
sizes = [
    sum(line.count('#') for line in lines[start:start+3])
    for start in range(1, 27, 5)
]

for line in lines[30:]:
    # Parse each line in an array of integers
    arr = list(map(int, re.split(r'x|: | ', line)))
    # Multiply the first two numbers => Total Area
    total_area = arr[0] * arr[1]
    # Multiply other numbers by their respective shape's size => Combined Shapes Area
    combined_shapes_area = sum(arr[i+2] * sizes[i] for i in range(6))
    # Simply check if the combined shapes area is bigger than total area
    remaining_area = total_area - combined_shapes_area
    if remaining_area >= 0:
        # It potentially fits in the total area
        answerp1 += 1
        # This is not strictly necessary but it tracks the closest call
        # meaning the line where there was "not much" area left after placing the shapes
        # Point is to show that it never was really close.
        # And we don't need to actually try to place the shapes
        # We just need to see if they would theoretically fit the area
        if remaining_area < closest_call:
            closest_call = remaining_area
            total_area_of_closest_call = total_area

print(f'ans: {answerp1}')
print(f'The closest call was: {closest_call} remaining area on a total area of: {total_area_of_closest_call}', file=sys.stderr)
print(f'Solved in: {datetime.now() - current_datetime}', file=sys.stderr)
