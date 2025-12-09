content = open(0).read()
boxes = [l.split(",") for l in content.splitlines()]


def euclidian_distance(box1, box2):
    X1, Y1, Z1 = map(int, box1)
    X2, Y2, Z2 = map(int, box2)
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
        return

    if size[root_x] < size[root_y]:
        parent[root_x] = root_y
        size[root_y] += size[root_x]
    else:
        parent[root_y] = root_x
        size[root_x] += size[root_y]


# Process the 1000 closest pairs (or 10 for small test sets)
num_pairs = 1000 if len(boxes) >= 100 else 10
for (i, j), distance in distances[:num_pairs]:
    union(i, j)

# Count cluster sizes
cluster_sizes = {}
for i in range(len(boxes)):
    root = find(i)
    cluster_sizes[root] = cluster_sizes.get(root, 0) + 1

# Get the 3 largest and multiply
sizes = sorted(cluster_sizes.values(), reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
