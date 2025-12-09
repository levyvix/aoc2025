content = open(0).read()
boxes = [l.split(",") for l in content.splitlines()]


def euclidian_distance(box1, box2):
    X1, Y1, Z1 = map(int, box1)
    X2, Y2, Z2 = map(int, box2)
    # Squared Euclidean distance (order preserved, avoids floating point)
    return (X1 - X2) ** 2 + (Y1 - Y2) ** 2 + (Z1 - Z2) ** 2


distances = {}
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = euclidian_distance(boxes[i], boxes[j])
        distances[(i, j)] = distance

# Sort distances by value
distances = sorted(distances.items(), key=lambda item: item[1])

# Union-Find structure
parent = list(range(len(boxes)))
size = [1] * len(boxes)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return False

    if size[root_x] < size[root_y]:
        parent[root_x] = root_y
        size[root_y] += size[root_x]
    else:
        parent[root_y] = root_x
        size[root_x] += size[root_y]

    return True


# Keep connecting until there's only 1 cluster
last_i, last_j = None, None
for (i, j), distance in distances:
    if union(i, j):
        last_i, last_j = i, j
        # Check if all boxes are now in the same cluster
        root = find(0)
        all_connected = all(find(box) == root for box in range(len(boxes)))
        if all_connected:
            break

# Get X coordinates of the last two connected boxes
x_i = int(boxes[last_i][0])
x_j = int(boxes[last_j][0])
print(x_i * x_j)
