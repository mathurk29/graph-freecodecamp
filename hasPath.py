# using DFS recursion
from collections import defaultdict


def hasPath_DFS(graph: dict, source: int, dest: int):
    # Base case
    if source == dest:
        return True

    # consider neighbors
    for neighbor in graph[source]:
        # Ifthere is path from THIS neighbor to dest
        if hasPath(graph, neighbor, dest):
            # there must be path from src to dest
            return True

    # Note: not doing below
    # # return hasPath(graph, neighbor, dest)
    # bcz we don't want to return False as may be there is path by some other neighbor

    # Now we have reached here so no path by any neighbor
    return False


# Using BFS (queue)
def hasPath_BFS(graph, source, dest):
    queue = [source]

    while queue:
        current_node = queue.pop()
        if current_node == dest:
            return True
        for neighbor in graph[current_node]:
            queue.append(neighbor)

    return False


def buildGraph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph


# Using DFS and recursion
def hasPathCyclic(graph: dict, source: int, dest: int, visited: set):
    # Base case
    if source in visited:
        return False
    visited.add(source)
    if source == dest:
        return True

    # consider neighbors
    for neighbor in graph[source]:
        # Ifthere is path from THIS neighbor to dest
        if hasPathCyclic(graph, neighbor, dest, visited):
            # there must be path from src to dest
            return True

    # Note: not doing below
    # # return hasPath(graph, neighbor, dest)
    # bcz we don't want to return False as may be there is path by some other neighbor

    # Now we have reached here so no path by any neighbor
    return False


def undirected_path(edges, src, dest):
    graph = buildGraph(edges)
    visited = set()
    return hasPathCyclic(graph, src, dest, visited)
