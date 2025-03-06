from data import books
graph = books
#target is current vertex
#value is target value


def dfs(graph, target, value, visited = None):
    if visited is None:
        visited = []
    visited.append(target)
    if target is value:
        return visited
    
    for neighbour in graph[target]:
        if neighbour not in visited:
            path = dfs(graph, neighbour, target, visited)
            if path:
                return path
    