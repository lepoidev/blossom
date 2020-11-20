from helpers import sorted_pair

# represents an undirected edge
class Edge:
    def __init__(self, start, end, num_nodes):
        self.start, self.end = sorted_pair(start, end)
        self.id = (self.start * num_nodes) + self.end

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return other.id == self.id

    def __repr__(self):
        return '{start=' + str(self.start) + ' end=' + str(self.end) + '}'

    def __contains__(self, item):
        return item == self.start or item == self.end


class Tree:
    def __init__(self, root):
        self.root  = root
        self.edges = set()
        self.nodes = {root}
        self.dists = {root : 0}
        self.parent_map = {root : None}

    def __repr__(self):
        return self.nodes.__repr__()

    def add(self, edge):
        if edge.start in self.nodes:
            new_node = edge.end
            old_node = edge.start
        else:
            new_node = edge.start
            old_node = edge.end

        self.nodes.add(new_node)

        self.edges.add(edge)

        self.dists[new_node] = self.dists[old_node] + 1

        self.parent_map[new_node] = old_node

    def has_node(self, node):
        return node in self.nodes

    def has_edge(self, edge):
        return edge in self.edges

    def dist_from_root(self, node):
        return self.dists[node]

    def path_to_root(self, node):
        path = []
        cur = node
        while cur is not None:
            path.insert(0, cur)
            cur = self.parent_map[cur]
        return path


def contract_edges(num_nodes, edges, B, blossom_root):
    contracted = set()

    B = set(B)

    for edge in edges:
        start = edge.start
        end = edge.end

        if start in B and end in B:
            continue

        if start in B and end not in B:
            start = blossom_root
        elif end in B and start not in B:
            end = blossom_root

        contracted.add(Edge(start, end, num_nodes))
    return contracted


class Matching:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = set()

    def __repr__(self):
        return self.edges.__repr__()

    def augment(self, path):
        add = True
        for i in range(0, len(path) - 1):
            j = i + 1
            start = path[i]
            end   = path[j]
            edge  = Edge(start, end, self.num_nodes)
            if add:
                self.edges.add(edge)
            elif edge in self.edges:
                self.edges.remove(edge)
            add = not add

    def get_contraction(self, B, blossom_root):
        contraction_M = Matching(self.num_nodes)
        contraction_M.edges = contract_edges(self.num_nodes, self.edges, B, blossom_root)
        return contraction_M

