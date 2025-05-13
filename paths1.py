from collections.abc import Iterator
from graph import*

def paths(graph: digraph, origin: node, destination: node) -> list[list[node]]:

    ''' assumes 'graph' is a graph containing origin and destination as 2 nodes
        returns a list of the valid paths between origin and destination

        works only for graphs without loops
        
        a valid path here is a orderd list of intermediate nodes terminated by destination
        such that one can sequentially traverse each proceeding node of the path through edges of the graph 
        starting from origin to end at destination'''

    assert origin in graph.get_nodes()
    assert destination in graph.get_nodes()

    paths = [] #this is what will be returned

    children = graph.get_children()
    iterator = { parent : iter(children[parent]) for parent in children}
    
    switch = iterator[origin]
    next_node = next(switch)
    path = [origin]
    backtrack_index = 0

    def backtrack(backtrack_index: int, path: list[node], switch: Iterator) -> tuple:
        if backtrack_index == -1:
            raise StopIteration
        try:
            path = path[ : backtrack_index + 1]
            next_node = next(switch)
            return next_node, path, switch, backtrack_index 
        except StopIteration:
            switch = iterator[path[backtrack_index - 1]]
            path = path[ : backtrack_index]
            backtrack_index  -= 1
            return backtrack(backtrack_index, path, switch)
        
    def track( path: list[node], switch: Iterator, backtrack_index: int) -> tuple:
        if len(children[path[-1]]) > 1:
            new_switch = iterator[path[-1]]
            next_node = next(new_switch)
            return next_node, new_switch, len(path) -1
        else:
            next_node = children[path[-1]][0]
            return next_node, switch, backtrack_index
        
    while True:
        print(path)
        try:
            path += [next_node]
            if next_node == destination:
                paths += [path]
                next_node, path, switch, backtrack_index = backtrack(backtrack_index, path, switch)
            elif children[next_node] == []:
                next_node, path, switch, backtrack_index = backtrack(backtrack_index, path, switch)
            else:
                next_node, switch, backtrack_index = track(path, switch, backtrack_index)
        except StopIteration:
            return paths
