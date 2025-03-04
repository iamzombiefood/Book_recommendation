from data import books 
def dfs(books, current_vertex, target_value, visited = None):
    if visited is None:
        visted = []
    visited.append(current_vertex)
    if current_vertex is target_value:
        return visited
    
    for neighbour in books[current_vertex]:
        if neighbour not in visited:
            path = dfs(books, neighbour, target_value, visited)
            if path:
                return path