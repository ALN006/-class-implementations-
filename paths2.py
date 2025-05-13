from graph import *



def paths(graph: digraph, origin: node, destination: node) -> list[list[node]]:


    ''' assumea 'graph' is digraph containing origin and destination as 2 nodes
        returns a list of valid paths between origin and destination as determined by dfs

        a valid path here is an orderd list of nodes such that one can sequentially traverse
        the nodes to end at destination'''
    

    assert origin in graph
    assert destination in graph

    paths = []

    children = graph.get_children()
    switch_stack = [iter(children[origin])]
    path_stack = [origin]

    while path_stack:

        try:

            next_node = next(switch_stack[-1])
            
            if next_node in path_stack:
                continue

            path_stack.append(next_node)
            switch_stack.append(iter(children[next_node]))

            if next_node == destination:
                paths.append(path_stack.copy())

        except StopIteration: 

            switch_stack.pop()
            path_stack.pop()


    return paths