def isSafe(graph, color, v, c):
    # Check for all adjacent vertices
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graphColoring(graph, m, color, v):
    # If all vertices are assigned a color then return True
    if v == len(graph):
        return True

    # Consider this vertex v and try different colors
    for c in range(1, m+1):
        # Check if assignment of color c to vertex v is safe
        if isSafe(graph, color, v, c):
            color[v] = c

            # Recur to assign colors to the next vertices
            if graphColoring(graph, m, color, v + 1):
                return True

            # If assigning color c doesn't lead to a solution, remove it (backtrack)
            color[v] = 0

    # If no color can be assigned to this vertex, return False
    return False

def main():
    n = int(input("Enter number of vertices: "))  # number of vertices
    m = int(input("Enter number of colors: "))  # number of colors
    print("Enter the adjacency matrix (0 for no edge, 1 for edge):")
    graph = []

    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    color = [0] * n  # Initialize all vertices with no color

    if graphColoring(graph, m, color, 0):
        print("Solution found:")
        for i in range(n):
            print(f"Vertex {i} → Color {color[i]}")
    else:
        print("No solution exists.")

if __name__ == '__main__':
    main()
