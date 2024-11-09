from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    output = []  # the order in which the nodes are visited 

    while queue:
        node = queue.popleft()
        if node not in visited:
            print (node, end='')
            visited.add(node)
            output.append(node)


            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return output

graph = {
    'A': ['S', 'D'],
    'B': ['D','S'],
    'S': ['A', 'B', 'C'], 
    'D': ['A', 'B', 'C'], 
    'C': ['S', 'D']
}

bfs(graph, 'S')