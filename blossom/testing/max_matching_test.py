import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from max_matching import max_matching
from structures import Edge, Tree, Matching
from graphing import find_and_show_max_matching

def complete_graph(n):
    edges = set()
    for i in range(n):
        for j in range(i + 1, n):
            edges.add(Edge(i, j, n))

    return n, list(range(n)), edges


def ex_1():
    n = 28
    nodes = list(range(1, n + 1))
    edges = set()
    edges.add(Edge(1,2,n))

    edges.add(Edge(2,3,n))
    edges.add(Edge(2,24,n))

    edges.add(Edge(3,4,n))
    edges.add(Edge(3,5,n))

    edges.add(Edge(5,6,n))

    edges.add(Edge(6,7,n))

    edges.add(Edge(7,8,n))
    edges.add(Edge(7,11,n))

    edges.add(Edge(8,9,n))

    edges.add(Edge(9,10,n))

    edges.add(Edge(10,13,n))

    edges.add(Edge(11,12,n))

    edges.add(Edge(12,13,n))

    edges.add(Edge(13,14,n))

    edges.add(Edge(14,15,n))
    edges.add(Edge(14,18,n))

    edges.add(Edge(15,16,n))

    edges.add(Edge(16,17,n))

    edges.add(Edge(17,18,n))

    edges.add(Edge(18,19,n))

    edges.add(Edge(19,20,n))

    edges.add(Edge(20,21,n))
    edges.add(Edge(20,26,n))

    edges.add(Edge(21,22,n))

    edges.add(Edge(22,23,n))

    edges.add(Edge(23,24,n))

    edges.add(Edge(24,25,n))

    edges.add(Edge(25,26,n))

    edges.add(Edge(26,27,n))

    edges.add(Edge(27,28,n))

    return n, nodes, edges


def ex_2():
    n = 37
    nodes = list(range(1, n + 1))
    edges = set()
    edges.add(Edge(1, 2, n))
    edges.add(Edge(1, 9, n))
    edges.add(Edge(1, 10, n))

    edges.add(Edge(2, 3, n))
    edges.add(Edge(2, 10, n))
    edges.add(Edge(2, 11, n))
    edges.add(Edge(2, 33, n))

    edges.add(Edge(3, 4, n))
    edges.add(Edge(3, 30, n))
    edges.add(Edge(3, 33, n))
    edges.add(Edge(3, 35, n))
    edges.add(Edge(3, 36, n))

    edges.add(Edge(4, 5, n))
    edges.add(Edge(4, 27, n))
    edges.add(Edge(4, 28, n))
    edges.add(Edge(4, 29, n))
    edges.add(Edge(4, 30, n))

    edges.add(Edge(5, 6, n))
    edges.add(Edge(5, 21, n))
    edges.add(Edge(5, 27, n))

    edges.add(Edge(6, 7, n))
    edges.add(Edge(6, 20, n))
    edges.add(Edge(6, 21, n))

    edges.add(Edge(7, 8, n))
    edges.add(Edge(7, 16, n))
    edges.add(Edge(7, 17, n))
    edges.add(Edge(7, 18, n))
    edges.add(Edge(7, 19, n))
    edges.add(Edge(7, 20, n))

    edges.add(Edge(8, 9, n))
    edges.add(Edge(8, 13, n))
    edges.add(Edge(8, 14, n))
    edges.add(Edge(8, 16, n))

    edges.add(Edge(9, 10, n))
    edges.add(Edge(9, 12, n))
    edges.add(Edge(9, 13, n))

    edges.add(Edge(10, 11, n))
    edges.add(Edge(10, 12, n))

    edges.add(Edge(11, 12, n))
    edges.add(Edge(11, 32, n))
    edges.add(Edge(11, 33, n))
    edges.add(Edge(11, 34, n))

    edges.add(Edge(12, 13, n))
    edges.add(Edge(12, 24, n))
    edges.add(Edge(12, 32, n))

    edges.add(Edge(13, 14, n))
    edges.add(Edge(13, 15, n))
    edges.add(Edge(13, 24, n))

    edges.add(Edge(14, 15, n))
    edges.add(Edge(14, 16, n))
    edges.add(Edge(14, 17, n))

    edges.add(Edge(15, 17, n))
    edges.add(Edge(15, 18, n))
    edges.add(Edge(15, 24, n))

    edges.add(Edge(16, 17, n))

    edges.add(Edge(17, 18, n))

    edges.add(Edge(18, 19, n))
    edges.add(Edge(18, 24, n))

    edges.add(Edge(19, 20, n))
    edges.add(Edge(19, 23, n))
    edges.add(Edge(19, 24, n))

    edges.add(Edge(20, 21, n))
    edges.add(Edge(20, 22, n))
    edges.add(Edge(20, 23, n))

    edges.add(Edge(21, 22, n))
    edges.add(Edge(21, 27, n))

    edges.add(Edge(22, 23, n))
    edges.add(Edge(22, 26, n))
    edges.add(Edge(22, 27, n))

    edges.add(Edge(23, 24, n))
    edges.add(Edge(23, 25, n))
    edges.add(Edge(23, 26, n))

    edges.add(Edge(24, 25, n))
    edges.add(Edge(24, 31, n))
    edges.add(Edge(24, 32, n))

    edges.add(Edge(25, 26, n))
    edges.add(Edge(25, 29, n))
    edges.add(Edge(25, 31, n))

    edges.add(Edge(26, 27, n))
    edges.add(Edge(26, 28, n))
    edges.add(Edge(26, 29, n))

    edges.add(Edge(27, 28, n))

    edges.add(Edge(28, 29, n))

    edges.add(Edge(29, 30, n))
    edges.add(Edge(29, 31, n))

    edges.add(Edge(30, 31, n))
    edges.add(Edge(30, 36, n))

    edges.add(Edge(31, 32, n))
    edges.add(Edge(31, 36, n))
    edges.add(Edge(31, 37, n))

    edges.add(Edge(32, 34, n))
    edges.add(Edge(32, 37, n))

    edges.add(Edge(33, 34, n))
    edges.add(Edge(33, 35, n))

    edges.add(Edge(34, 35, n))
    edges.add(Edge(34, 37, n))

    edges.add(Edge(35, 36, n))
    edges.add(Edge(35, 37, n))

    edges.add(Edge(36, 37, n))

    return n, nodes, edges


def test_edge():
    n, nodes, edges = complete_graph(10)

    for i in range(n):
        for j in range(i + 1, n):
            assert Edge(i, j, n) in edges
            assert Edge(j, i, n) in edges

def test_base_cases():
    n, nodes, edges = 1, [1], set()
    matching = max_matching(nodes, edges)
    matches = len(matching.edges)
    assert matches == 0

    n, nodes, edges = 2, [1,2], {Edge(1, 2, 2)}
    matching = max_matching(nodes, edges)
    matches = len(matching.edges)
    assert matches == 1

def test_ex_1():
    n, nodes, edges = ex_1()
    matching = max_matching(nodes, edges)
    matches = len(matching.edges)
    assert matches == 14

def test_ex_2():
    n, nodes, edges = ex_2()
    matching = max_matching(nodes, edges)
    matches = len(matching.edges)
    wrong_edges = matching.edges - edges
    assert len(wrong_edges) == 0
    assert matches == 18

def test_completed_graph():
    for k in range(1, 50):
        n, nodes, edges = complete_graph(k)
        matching = max_matching(nodes, edges)
        matches = len(matching.edges)
        assert matches == (n // 2)

if __name__ == "__main__":
    test_edge()

    test_base_cases()

    test_ex_1()

    test_ex_2()

    test_completed_graph()

    # here is an example of displaying a max matching
    # n, nodes, edges = ex_2()
    # find_and_show_max_matching(n, nodes, edges)

    print('Passed')