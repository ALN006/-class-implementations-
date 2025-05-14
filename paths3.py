from graph import *


def paths(graph: digraph, origin: node, destination: node) -> list[list[node]]:
    
    ''' Returns all valid paths from origin to destination in a digraph using DFS.
        Avoids cycles by tracking visited nodes. '''

    assert origin in graph
    assert destination in graph

    paths = []
    children = graph.get_children()

    def dfs(current: node, path: list[node], visited: set) -> list[node]:

        path.append(current)

        if current == destination:
            paths.append(path.copy())
            return
        
        else:
            for child in children[current]:
                if child in visited: continue
                visited.add(child)
                dfs(child,path, visited)
                visited.remove(child)
                path.pop()

    dfs(origin,[],set())
    return paths

