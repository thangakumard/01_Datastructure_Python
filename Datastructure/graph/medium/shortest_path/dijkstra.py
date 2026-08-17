'''
Dijkstra's Shortest Path Algorithm

Given a weighted, directed graph and a source node, find the shortest path
from the source to every other node (and print the path to a specific target).

Example graph:
        10
    A -------> B
    |          |
   5|         1|
    v    3     v
    C -------> D

Shortest path from A to D: A -> C -> D with cost 8

Algorithm: Greedy BFS using a min-heap (priority queue)
============================================================
1. Initialize dist[source] = 0, all others = infinity
2. Push (0, source) into the min-heap
3. Pop the node with smallest tentative distance
4. For each neighbor, relax the edge: if dist[node] + weight < dist[neighbor],
   update dist[neighbor] and record prev[neighbor] = node
5. Repeat until heap is empty
6. Reconstruct path by backtracking through prev[]

Complexity:
============
Time:  O((V + E) log V) — each node/edge processed once with heap ops
Space: O(V) for dist[], prev[], and the heap
'''

import heapq
from typing import Optional


def dijkstra(graph: dict[str, list[tuple[str, int]]], source: str) -> tuple[dict, dict]:
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    prev: dict[str, Optional[str]] = {node: None for node in graph}

    heap = [(0, source)]

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_cost = dist[node] + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = node
                heapq.heappush(heap, (new_cost, neighbor))

    return dist, prev


def reconstruct_path(prev: dict, source: str, target: str) -> list[str]:
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev.get(node)
    path.reverse()
    if path[0] != source:
        return []  # target unreachable
    return path


def shortest_path(
    graph: dict[str, list[tuple[str, int]]], source: str, target: str
) -> tuple[list[str], float]:
    dist, prev = dijkstra(graph, source)
    if dist[target] == float('inf'):
        return [], float('inf')
    path = reconstruct_path(prev, source, target)
    return path, dist[target]


# ── Tests ──────────────────────────────────────────────────────────────────────

def test_simple_path():
    graph = {
        'A': [('B', 10), ('C', 5)],
        'B': [('D', 1)],
        'C': [('B', 3), ('D', 9)],
        'D': [],
    }
    path, cost = shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D'], f"Expected A->C->B->D, got {path}"
    assert cost == 9, f"Expected cost 9, got {cost}"
    print("test_simple_path passed")


def test_direct_edge_beats_longer_path():
    graph = {
        'A': [('B', 1), ('C', 10)],
        'B': [('C', 1)],
        'C': [],
    }
    path, cost = shortest_path(graph, 'A', 'C')
    assert path == ['A', 'B', 'C'], f"Expected A->B->C, got {path}"
    assert cost == 2, f"Expected cost 2, got {cost}"
    print("test_direct_edge_beats_longer_path passed")


def test_source_equals_target():
    graph = {
        'A': [('B', 5)],
        'B': [],
    }
    path, cost = shortest_path(graph, 'A', 'A')
    assert path == ['A'], f"Expected ['A'], got {path}"
    assert cost == 0, f"Expected cost 0, got {cost}"
    print("test_source_equals_target passed")


def test_unreachable_target():
    graph = {
        'A': [('B', 3)],
        'B': [],
        'C': [],
    }
    path, cost = shortest_path(graph, 'A', 'C')
    assert path == [], f"Expected empty path, got {path}"
    assert cost == float('inf'), f"Expected inf cost, got {cost}"
    print("test_unreachable_target passed")


def test_all_distances():
    graph = {
        'S': [('A', 4), ('B', 2)],
        'A': [('C', 5)],
        'B': [('A', 1), ('C', 8)],
        'C': [],
    }
    dist, _ = dijkstra(graph, 'S')
    assert dist['S'] == 0
    assert dist['A'] == 3   # S->B->A
    assert dist['B'] == 2   # S->B
    assert dist['C'] == 8   # S->B->A->C
    print("test_all_distances passed")


if __name__ == '__main__':
    test_simple_path()
    test_direct_edge_beats_longer_path()
    test_source_equals_target()
    test_unreachable_target()
    test_all_distances()

    # Demo
    graph = {
        'A': [('B', 10), ('C', 5)],
        'B': [('D', 1)],
        'C': [('B', 3), ('D', 9)],
        'D': [],
    }
    path, cost = shortest_path(graph, 'A', 'D')
    print(f"\nShortest path A -> D: {' -> '.join(path)} (cost {cost})")
