def paths(graph, origin, destination):   
    path = []
    paths = []

    def dfs(current,visited: set):
        
        path.append(current)

        if path[0] == origin and path[-1] == destination:
            paths.append(path.copy())
        else:
            visited.add(current)

            for child in graph[current]:
                if child not in visited:
                    dfs(child,  visited)

            visited.remove(current)
        path.pop()
    
    dfs(origin,set())
    return paths
