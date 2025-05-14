
class node(object):

    """ self is a node of a graph, IE an entity possesing: 1.data 2.parent nodes 3.child nodes """


    def __init__(self: "node", data: object) -> None:

        self.data = data


    def __eq__(self: "node", other: "node") -> bool:

        return self.data == other.data
    

    def __repr__(self: "node") -> str:

        return str(self.data)
    
    
    def __hash__(self:"node") -> int:

        return hash(self.data)
    

    def get_data(self: "node") -> object:

        return self.data



class edge(object):

    """ self is a weighted unidirectional connection between 2 nodes of a graph """


    def __init__(self: "edge", weight: float, origin: "node", destination: "node") -> None:
        
        self.weight = weight
        self.origin = origin
        self.destination = destination


    def __repr__(self: "edge") -> str:

        return str(self.origin) + "--" + str(self.weight) + "->" + str(self.destination)


    def get_weight(self: "edge") -> float:

        return self.weight
    

    def get_origin(self: "edge") -> "node":

        return self.origin
    
    
    def get_destination(self: "edge") -> "node":

        return self.destination



class digraph(object):

    ''' self is a collection of consistend nodes and edges'''


    def __init__(self: "digraph", nodes: set["node"], edges: list["edge"]) -> None:
        
        self.nodes = nodes
        self.edges = edges


    def __repr__(self: "digraph") -> str:
        ''' I dont know how to do this well'''

        return ""
    

    def __contains__(self: "digraph", node: "node") -> bool:

        return node in self.nodes


    def add_node(self: "digraph", add_type: str, new_node: "node", old_node: "node", edge_weight: float) -> None:
        
        assert old_node in self.nodes
        assert add_type in ("parent", "child")

        if add_type == "parent": 
            self.edges += [edge(edge_weight, new_node, old_node)] #because parent comes first in edge initialization
        else:
            self.edges += [edge(edge_weight, old_node, new_node)]
        self.nodes.add(new_node)
    

    def remove_node(self: "digraph", gone: "node") -> None:

        self.nodes = set( node for node in self.nodes if node != gone )
        self.edges = [ edge for edge in self.edges if (edge.get_origin() != gone and edge.get_destination() != gone)]


    def get_nodes(self: "digraph") -> set["node"]:
        
        return self.nodes
    

    def get_edges(self: "digraph") -> list["edge"]:

        return self.edges
    
    
    def get_children(self: "digraph") -> dict["node",list["node"]]:

        ans = { node : [] for node in self.nodes}

        for edge in self.edges:
            ans[edge.get_origin()] += [edge.get_destination()]

        return ans


    def dfs(self: "digraph", origin: "node", destination: "node") -> list[list["node"]]:

        ''' self is digraph containing origin and destination as 2 nodes
            returns a list of valid paths between origin and destination as determined by dfs

            a valid path here is an orderd list of nodes such that one can sequentially traverse
            the nodes to end at destination'''

        assert origin in self.nodes
        assert destination in self.nodes

        paths = []

        children = self.get_children()
        switch_stack = [iter(children[origin])]
        path_stack = [origin]
        visited = set(path_stack)

        while path_stack:
            try:
                next_node = next(switch_stack[-1])
                if next_node in visited:
                    continue
                path_stack.append(next_node)
                switch_stack.append(iter(children[next_node]))
                visited.add(next_node)
                if next_node == destination:
                    paths.append(path_stack.copy())
            except StopIteration:
                switch_stack.pop()
                visited.remove(path_stack.pop())
        return paths


class graph(digraph):

    ''' self is a digraph with all connections being 2 way'''

    
    def add_node(self: "digraph", new_node: "node", old_node: "node", out_weight: float, in_weight: float) -> None:
        
        assert old_node in self.nodes
        assert new_node not in self.nodes

        self.edges += [edge(out_weight, old_node, new_node)]
        self.edges += [edge(in_weight, new_node, old_node)]
        self.nodes.add(new_node)
