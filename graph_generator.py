import random


def generate_graph(num_vertices, edge_probability=0.2, seed=None):
    if num_vertices < 1:
        raise ValueError("num_vertices must be at least 1")

    rng = random.Random(seed)

    graph = {node: [] for node in range(num_vertices)}

    # First, connect every vertex to ensure connectivity.
    for node in range(1, num_vertices):
        parent = rng.randrange(node)
        weight = rng.randint(1, 20)

        graph[node].append((parent, weight))
        graph[parent].append((node, weight))

    # Then, add extra edges randomly.
    for u in range(num_vertices):
        for v in range(u + 1, num_vertices):
            if not any(neighbor == v for neighbor, _ in graph[u]):
                if rng.random() < edge_probability:
                    weight = rng.randint(1, 20)
                    graph[u].append((v, weight))
                    graph[v].append((u, weight))

    return graph


if __name__ == "__main__":
    graph = generate_graph(5, seed=42)

    for node, neighbors in graph.items():
        print(node, "->", neighbors)