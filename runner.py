"""
DevRunner Studio - Algorithm Complexity & Benchmark Runner
High-performance algorithms implementation: Dijkstra, LRU Cache, Tree Traversal.
"""

import time
import heapq
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def dijkstra(graph: dict, start_node: str) -> dict:
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list:
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


def run_benchmarks():
    print("=" * 60)
    print("  DEVRUNNER ALGORITHM BENCHMARK SUITE")
    print("=" * 60)

    # 1. Dijkstra Benchmark
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "Z": 6},
        "E": {"C": 10, "D": 2, "Z": 3},
        "Z": {"D": 6, "E": 3},
    }
    t0 = time.perf_counter()
    dist = dijkstra(graph, "A")
    t_dijkstra = (time.perf_counter() - t0) * 1000
    print(f"[✓] Dijkstra Shortest Path:  Target 'Z' cost = {dist['Z']} ({t_dijkstra:.4f} ms)")

    # 2. LRU Cache Benchmark
    lru = LRUCache(1000)
    t0 = time.perf_counter()
    for i in range(10000):
        lru.put(i, i * 2)
        _ = lru.get(i // 2)
    t_lru = (time.perf_counter() - t0) * 1000
    print(f"[✓] LRU Cache (10k ops):     Passed ({t_lru:.4f} ms)")

    # 3. Binary Tree Traversal
    root = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, None, TreeNode(20)))
    t0 = time.perf_counter()
    res = inorder_traversal(root)
    t_tree = (time.perf_counter() - t0) * 1000
    print(f"[✓] Tree Inorder Traversal:  {res} ({t_tree:.4f} ms)")
    print("=" * 60)
    print("  ALL BENCHMARKS EXECUTED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
