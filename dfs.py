# Define a simple graph using a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS function using a stack
def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Stack for DFS, start with the initial node

    while stack:
        node = stack.pop()  # Get the last node from the stack
        if node not in visited:
            print(node, end=" ")  # Print the node (or do something with it)
            visited.add(node)  # Mark the node as visited
            # Add neighbors of the node to the stack if not visited
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Run DFS starting from node 'A'
if __name__=="__main__":
    dfs(graph, 'A')

