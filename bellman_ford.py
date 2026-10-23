def bellman_ford(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((node, neighbor, weight))

    for _ in range(len(graph) - 1):
        updated = False

        for u, v, weight in edges:
            if distances[u] != float('inf'):
                distance = distances[u] + weight

                if distance < distances[v]:
                    distances[v] = distance
                    updated = True

        if not updated:
            break

    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a reachable negative-weight cycle")

    return distances


if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8)],
        'D': [('B', 5), ('C', 8)]
    }

    print(bellman_ford(graph, 'A'))