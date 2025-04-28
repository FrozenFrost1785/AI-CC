def recursive_bfs(graph, visited, queue):
    if not queue:
        return
    node = queue.pop(0)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
    recursive_bfs(graph, visited, queue)

def recursive_dfs(graph, visited, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            recursive_dfs(graph, visited, neighbour)

def main():
    n = int(input("Enter the number of nodes: "))
    graph = dict()
    for i in range(1, n + 1):
        edges = int(input(f"Enter the number of edges for node {i}: "))
        graph[i] = []
        for j in range(edges):
            node = int(input(f"Enter edge {j+1} for node {i}: "))
            graph[i].append(node)

    while True:
        choice = int(input("Enter the operation (1=BFS, 2=DFS, 3=Exit): "))
        if choice == 1:
            start = int(input("Enter the starting node for BFS: "))
            visited = [start]
            queue = [start]
            print("Recursive BFS:", end=" ")
            recursive_bfs(graph, visited, queue)
            print()
        elif choice == 2:
            start = int(input("Enter the starting node for DFS: "))
            visited = []
            print("Recursive DFS:", end=" ")
            recursive_dfs(graph, visited, start)
            print()
        elif choice == 3:
            exit()
        else:
            print("Enter a valid input.")

if __name__ == "__main__":
    main()
