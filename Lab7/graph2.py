import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Heuristic values
heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': float('inf'), 'E': float('inf'), 'G': 0}

# Define edges and weights
edges = {
    'S': [('A', 1), ('B', 5), ('C', 8)],
    'A': [('S', 1), ('D', 3), ('E', 7), ('G', 9)],
    'B': [('S', 5), ('G', 4)],
    'C': [('S', 8), ('G', 5)],
    'D': [('A', 3)],
    'E': [('A', 7)],
    'G': [('A', 9), ('B', 4), ('C', 5)]
}

# A* Algorithm
def astar(start, goal):
    open_list = [(0, start)]
    g = {start: 0}
    parents = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for neighbor, cost in edges.get(current, []):
            tentative_g = g[current] + cost
            if tentative_g < g.get(neighbor, float('inf')):
                g[neighbor] = tentative_g
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parents[neighbor] = current
    return None


# Run A*
path = astar('S', 'G')
print("Shortest path found by A*:", path)

# Visualization
G = nx.DiGraph()
for node in edges:
    for neighbor, cost in edges[node]:
        G.add_edge(node, neighbor, weight=cost)

pos = nx.spring_layout(G, seed=5)
nx.draw(G, pos, with_labels=True, node_color="#e06666", node_size=1500, font_size=14, font_weight='bold', arrows=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

plt.title("A* Pathfinding Graph 2")
plt.show()

