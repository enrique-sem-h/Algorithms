# Implemente uma função que, dado um nó inicial (uma pessoa), use BFS para encontrar a menor distância em número de arestas entre essa pessoa e todas as outras do grafo.
from collections import deque

def search(graph, start):
    queue = deque([start])
    verified = {start : 0}

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in verified:
                verified[neighbor] = verified[current] + 1
                queue.append(neighbor)
    return verified

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

print(search(graph, "F"))
