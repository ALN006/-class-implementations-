from graph import *

def dfs(children, path, objective, res: list[node], visited, stack):

    if objective(path) < objective(res):
        res = path.copy()
    
    visited.add(path[-1])
    
    for child in children[path[-1]]:
        if child not in visited:
            path.append(child)
            dfs(children, path, objective, res, visited)
            path.pop()

    visited.remove(path[-1])

    return res