def aStarAlgo(start_node, stop_node):
    """
    A simple A* implementation using sets for OPEN/CLOSED.
    Returns the path as a list of nodes from start_node to stop_node, or None if no path.
    """
    # OPEN holds nodes to explore; CLOSED holds already-explored nodes
    open_set = set([start_node])
    closed_set = set()

    # g: cost from start to node
    g = {}
    # parents: used to reconstruct path
    parents = {}

    # initialize
    g[start_node] = 0
    parents[start_node] = None

    while len(open_set) > 0:
        # select node in OPEN with lowest f(n) = g(n) + h(n)
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If no node found (shouldn't happen), no path exists
        if n is None:
            return None

        # If we reached the goal, reconstruct path
        if n == stop_node:
            path = []
            while n is not None:
                path.append(n)
                n = parents[n]
            path.reverse()
            return path

        # Explore neighbors of n
        for (m, weight) in get_neighbors(n):
            # tentative g score to neighbor m through n
            tentative_g = g[n] + weight

            # if neighbor not seen before
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = tentative_g

            else:
                # if this path to m is better, update
                if tentative_g < g.get(m, float('inf')):
                    g[m] = tentative_g
                    parents[m] = n

                    # if m was already evaluated, move it back to open_set
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # move n from OPEN to CLOSED
        open_set.remove(n)
        closed_set.add(n)

    # OPEN exhausted and no path found
    return None


def get_neighbors(v):
    """Return list of (neighbor, weight) pairs. Return empty list if node not present."""
    return Graph_nodes.get(v, [])


def heuristic(n):
    """Heuristic function (h)."""
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    # If node not in heuristic table, assume large heuristic (or 0 depending on use-case)
    return H_dist.get(n, 0)


Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': []
}


# Example run
if __name__ == "__main__":
    path = aStarAlgo('A', 'H')
    if path:
        print("Path found:", path)
    else:
        print("Path does not exist!")


#################################################################################################
######################################## PseudoCode ############################################

# A*(start, goal):
#
#. open_set = {start}
#. closed_set = {}
#
#. g(start) = 0
#. parent(start) = None
#
#. while open_set is not empty:
#.     n = node in open_set with lowest f(n) = g(n) + h(n)
#
#.     if n == goal:
#.         return path reconstructed from parents
#
#.     for each neighbor m of n:
#0.         tentative_g = g(n) + distance(n, m)
#1.         if m not in open_set or tentative_g < g(m):
#2.             parent(m) = n
#3.             g(m) = tentative_g
#4.             add m to open_set

#5.     remove n from open_set
#6.     add n to closed_set

#7. if goal not reached:
#8.     return None
