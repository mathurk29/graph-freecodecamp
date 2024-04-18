# only queue is possible


def BFS(graph, source):
    queue = [source]  # Initialise

    while queue:

        # Pop  current node
        current_item = queue.pop()

        print(current_item)

        # Push neighbors
        for neighbor in graph[source]:
            queue.push(neighbor)
