# I have been struggling to learn BFS for a while now. Finally got it to work.
# This implementation takes a search element in a graph and returns it layered by the search
from collections import deque

def bfs(graph, search):
    dist = {search : 0}
    queue = deque([search])

    while queue:
        current_element = queue.popleft()
        for neighbor in graph[current_element]:
            if neighbor not in dist:
                dist[neighbor] = dist[current_element] + 1
                queue.append(neighbor)
    
    return dist



graph1 = {
    1 : [18, 54, 60],
    18 : [1],
    54 : [1],
    60 : [77, 1],
    77 : [100, 60],
    100 : [77]
}

print(bfs(graph1, 60))