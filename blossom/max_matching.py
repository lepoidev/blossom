from structures import Edge, Tree, Matching, contract_edges

def find_augmenting_path(num_nodes, nodes, edges, M):
    # find the matched edge in M which contains node and return its partner
    def find_match(node):
        for edge in M.edges:
            if node in edge:
                if node == edge.start:
                    return edge.end
                else:
                    return edge.start
        return None

    forest = [Tree(node) for node in nodes if find_match(node) is None]

    # find tree in the forest which contains the node
    def find_tree(node):
        for tree in forest:
            if tree.has_node(node):
                return tree
        return None

    # check if there exists and edge from start to end in the set of edges - M
    def edge_in_E_minus_M(start, end):
        edge = Edge(start, end, num_nodes)
        return (edge in edges) and (edge not in M.edges)

    unmarked_nodes = set(nodes)
    unmarked_edges = edges - M.edges

    while len(unmarked_nodes) > 0:
        v = unmarked_nodes.pop()
        v_tree = find_tree(v)
        # verify v is in forest and has an even distance to root
        if v_tree is None or not (v_tree.dist_from_root(v) % 2 == 0):
            continue

        edges_to_mark = set()
        for edge in unmarked_edges:
            if v not in edge:
                continue

            w = edge.start
            if v == edge.start:
                w = edge.end

            w_tree = find_tree(w)
            if w_tree is None:
                # we can add the matched edge to the tree
                x = find_match(w)
                v_tree.add(Edge(v, w, num_nodes))
                v_tree.add(Edge(w, x, num_nodes))
            else:
                if w_tree.dist_from_root(w) % 2 == 0:
                    w_to_root = w_tree.path_to_root(w)
                    w_to_root.reverse()
                    if v_tree.root != w_tree.root:
                        # return the augmenting path which runs from root of v -> v -> w -> root of w
                        return v_tree.path_to_root(v) + w_to_root
                    else:
                        # we have found a blossom
                        B = v_tree.path_to_root(v) + w_to_root[:-1]
                        blossom_len = len(B)
                        blossom_root = v_tree.root

                        # contract the blossom and to the blossom root
                        contracted_nodes = [node for node in nodes if node == blossom_root or node not in B]
                        contracted_edges = contract_edges(num_nodes, edges, B, blossom_root)
                        contracted_M     = M.get_contraction(B, blossom_root)

                        # recurse on contracted graph
                        contracted_path = find_augmenting_path(num_nodes, contracted_nodes, contracted_edges, contracted_M)
                        if contracted_path is None:
                            return None

                        try:
                            blossom_root_idx = contracted_path.index(blossom_root)
                        except ValueError:
                            return contracted_path

                        contracted_path_len = len(contracted_path)

                        enter_blossom_from_right = blossom_root_idx >= (contracted_path_len // 2)

                        # find nodes to the left and right of the blossom
                        left_of_blossom, right_of_blossom = None, None
                        if blossom_root_idx > 0:
                            left_of_blossom = contracted_path[blossom_root_idx - 1]

                        if blossom_root_idx < contracted_path_len - 1:
                            right_of_blossom = contracted_path[blossom_root_idx + 1]

                        # find which node connects to the blossom root and which node the blossom must exit to
                        if enter_blossom_from_right:
                            before_blossom, after_blossom = right_of_blossom, left_of_blossom
                        else:
                            before_blossom, after_blossom = left_of_blossom, right_of_blossom

                        # resolve path taken through the blossom
                        if (before_blossom, after_blossom) == (None, None):
                            path = B
                        else:
                            path = []

                            # find node in the blossom which connects to after_blossom
                            offset = 1
                            dist_from_root = 0
                            while offset <= (blossom_len // 2):
                                for cur_dist in [offset, blossom_len - offset]:
                                    blossom_node = B[cur_dist]
                                    if edge_in_E_minus_M(blossom_node, after_blossom):
                                        dist_from_root = cur_dist
                                        break
                                offset += 2

                            # find the path through the blossom
                            if dist_from_root == 0:
                                path = [blossom_root]
                            elif dist_from_root % 2 == 0:
                                # path is in direction of B
                                path = [B[i] for i in range(dist_from_root + 1)]
                            else:
                                # path is in reverse direction of B
                                path = [B[-i] for i in range(blossom_len + 1 - dist_from_root)]

                        if enter_blossom_from_right:
                            path.reverse()

                        # lifting
                        path = contracted_path[:blossom_root_idx] + path + contracted_path[blossom_root_idx + 1:]
                        return path

            edges_to_mark.add(edge)
        unmarked_edges -= edges_to_mark
    return None


def find_max_matching(num_nodes, nodes, edges, M):
    path = find_augmenting_path(num_nodes, nodes, edges, M)
    if path is not None:
        M.augment(path)
        return find_max_matching(num_nodes, nodes, edges, M)
    return M


# using Edmonds Blossom algorithm for maximum matchings
# based on pseudocode in https://en.wikipedia.org/wiki/Blossom_algorithm
def max_matching(nodes, edges):
    num_nodes = len(nodes)
    M = Matching(num_nodes)
    return find_max_matching(num_nodes, nodes, edges, M)
