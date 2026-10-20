import pytest
from runner import LRUCache, dijkstra, TreeNode, inorder_traversal


def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    assert cache.get(1) == 100
    cache.put(3, 300)  # вытесняет ключ 2
    assert cache.get(2) == -1
    assert cache.get(3) == 300


def test_dijkstra_shortest_path():
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    distances = dijkstra(graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == 3
    assert distances["D"] == 4


def test_inorder_traversal():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    assert inorder_traversal(root) == [1, 2, 3, 4, 5]
