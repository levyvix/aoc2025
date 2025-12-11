from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

content = open(0).read()

# Parse the graph
graph = {}
for line in content.strip().split('\n'):
    device, outputs = line.split(': ')
    graph[device] = outputs.split()

# Count all paths from 'you' to 'out' using DFS
def count_paths(start, end, graph):
    def dfs(node, visited):
        if node == end:
            return 1

        total = 0
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                total += dfs(neighbor, visited)
                visited.remove(neighbor)

        return total

    return dfs(start, {start})

result = count_paths('you', 'out', graph)
print(result)