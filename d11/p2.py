from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

content = open(0).read()

# Parse the graph
graph = {}
for line in content.strip().split('\n'):
    device, outputs = line.split(': ')
    graph[device] = outputs.split()

# Use memoization to count paths visiting both required nodes
# Since the graph is acyclic, we can use memoization with just (node, visited_required_set)
memo = {}

def count_paths_visiting_both(node, end, required_nodes):
    def dfs(node, visited_required):
        if node == end:
            return 1 if len(visited_required) == len(required_nodes) else 0

        # Create a hashable key for memoization
        key = (node, frozenset(visited_required))
        if key in memo:
            return memo[key]

        total = 0
        for neighbor in graph.get(node, []):
            new_visited_required = visited_required.copy()
            if neighbor in required_nodes:
                new_visited_required.add(neighbor)
            total += dfs(neighbor, new_visited_required)

        memo[key] = total
        return total

    return dfs(node, set())

result = count_paths_visiting_both('svr', 'out', {'dac', 'fft'})
print(result)
