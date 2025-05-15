def paths(graph, origin, passes, weight):
    


    path = []
    paths = []



    def dfs(current,visited):


        path.append(current)


        if passes(path) == True:

            paths.append(path.copy())

        else:

            visited.add(current)

            for child in graph[current]:
                if child not in visited:
                    dfs(child, visited)

            visited.remove(current)


        path.pop()



    dfs(origin, set())



    ans = paths[0]


    for i in range(1,len(paths)):
        
        if weight(paths[i]) < weight(ans):
            ans = paths[i]



    return ans