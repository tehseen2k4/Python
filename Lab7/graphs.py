import networkx as nx
import matplotlib.pyplot as plt
import math
import random

# -------------------------------
# Helper: Euclidean heuristic
# -------------------------------
def euclidean_heuristic(u, v, pos):
    (x1, y1) = pos[u]
    (x2, y2) = pos[v]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# -------------------------------
# 1️⃣ Balanced Tree
# -------------------------------
G1 = nx.balanced_tree(r=2, h=3)
pos1 = nx.spring_layout(G1, seed=5)
for (u, v) in G1.edges():
    G1.edges[u, v]['weight'] = random.randint(1, 10)

path1 = nx.astar_path(G1, 0, max(G1.nodes()), heuristic=lambda u, v: euclidean_heuristic(u, v, pos1), weight='weight')
print("Balanced Tree Path:", path1)

plt.figure(figsize=(5, 4))
nx.draw(G1, pos1, with_labels=True, node_color="lightcoral", node_size=800)
nx.draw_networkx_edge_labels(G1, pos1, edge_labels=nx.get_edge_attributes(G1, 'weight'))
plt.title("A* on Balanced Tree")
plt.show()


# -------------------------------
# 2️⃣ Full r-ary Tree
# -------------------------------
G2 = nx.full_rary_tree(r=3, n=10)
pos2 = nx.spring_layout(G2, seed=10)
for (u, v) in G2.edges():
    G2.edges[u, v]['weight'] = random.randint(1, 10)

path2 = nx.astar_path(G2, 0, max(G2.nodes()), heuristic=lambda u, v: euclidean_heuristic(u, v, pos2), weight='weight')
print("Full r-ary Tree Path:", path2)

plt.figure(figsize=(5, 4))
nx.draw(G2, pos2, with_labels=True, node_color="lightblue", node_size=800)
nx.draw_networkx_edge_labels(G2, pos2, edge_labels=nx.get_edge_attributes(G2, 'weight'))
plt.title("A* on Full r-ary Tree")
plt.show()


# -------------------------------
# 3️⃣ Barbell Graph
# -------------------------------
G3 = nx.barbell_graph(m1=4, m2=3)
pos3 = nx.spring_layout(G3, seed=2)
for (u, v) in G3.edges():
    G3.edges[u, v]['weight'] = random.randint(1, 10)

path3 = nx.astar_path(G3, 0, max(G3.nodes()), heuristic=lambda u, v: euclidean_heuristic(u, v, pos3), weight='weight')
print("Barbell Graph Path:", path3)

plt.figure(figsize=(5, 4))
nx.draw(G3, pos3, with_labels=True, node_color="lightgreen", node_size=800)
nx.draw_networkx_edge_labels(G3, pos3, edge_labels=nx.get_edge_attributes(G3, 'weight'))
plt.title("A* on Barbell Graph")
plt.show()


# -------------------------------
# 4️⃣ Complete Graph
# -------------------------------
G4 = nx.complete_graph(6)
pos4 = nx.circular_layout(G4)
for (u, v) in G4.edges():
    G4.edges[u, v]['weight'] = random.randint(1, 10)

path4 = nx.astar_path(G4, 0, max(G4.nodes()), heuristic=lambda u, v: euclidean_heuristic(u, v, pos4), weight='weight')
print("Complete Graph Path:", path4)

plt.figure(figsize=(5, 4))
nx.draw(G4, pos4, with_labels=True, node_color="plum", node_size=800)
nx.draw_networkx_edge_labels(G4, pos4, edge_labels=nx.get_edge_attributes(G4, 'weight'))
plt.title("A* on Complete Graph")
plt.show()


# -------------------------------
# 5️⃣ Random Geometric Graph
# -------------------------------
G5 = nx.random_geometric_graph(10, radius=0.5)
pos5 = nx.get_node_attributes(G5, 'pos')
for (u, v) in G5.edges():
    G5.edges[u, v]['weight'] = euclidean_heuristic(u, v, pos5)

# Ensure graph is connected
nodes = list(G5.nodes())
start, goal = nodes[0], nodes[-1]

try:
    path5 = nx.astar_path(G5, start, goal, heuristic=lambda u, v: euclidean_heuristic(u, v, pos5), weight='weight')
    print("Random Geometric Graph Path:", path5)
except nx.NetworkXNoPath:
    print("No path exists between chosen nodes in random graph")

plt.figure(figsize=(5, 4))
nx.draw(G5, pos5, with_labels=True, node_color="gold", node_size=800)
nx.draw_networkx_edge_labels(G5, pos5, edge_labels=nx.get_edge_attributes(G5, 'weight'))
plt.title("A* on Random Geometric Graph")
plt.show()
