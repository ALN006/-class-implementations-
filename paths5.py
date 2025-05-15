
def dfs(graph, origin):

    stack = [origin]
    visited = set()

    while stack:

        current = stack.pop()

        #some condition on current 
        visited.add(current)
        
        stack.extend(graph[current])



