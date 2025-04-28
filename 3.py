import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to the start node is 0

    # Priority queue: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we already found a shorter path before, skip
        if current_distance > distances[current_node]:
            continue

        # Check neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If this path is shorter, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Define the graph as an adjacency list
graph = {
    'A': [('B', 7), ('C', 9), ('F', 14)],
    'B': [('A', 7), ('C', 10), ('D', 15)],
    'C': [('A', 9), ('B', 10), ('D', 11), ('F', 2)],
    'D': [('B', 15), ('C', 11), ('E', 6)],
    'E': [('D', 6), ('F', 9)],
    'F': [('A', 14), ('C', 2), ('E', 9)]
}

# Run Dijkstra's algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')

# Print results
print("Shortest distances from node A:")
for node, distance in shortest_paths.items():
    print(f"  A → {node}: {distance}")
