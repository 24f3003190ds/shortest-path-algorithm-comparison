import time
import csv

from dijkstra import dijkstra
from bellman_ford import bellman_ford
from graph_generator import generate_graph


graph_sizes = [50, 100, 150, 200, 300, 400, 500, 600]
repeats = 3

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "vertices",
        "dijkstra_time",
        "bellman_ford_time"
    ])

    for size in graph_sizes:
        graph = generate_graph(
            size,
            edge_probability=0.02,
            seed=42
        )

        dijkstra_times = []
        bellman_ford_times = []

        for _ in range(repeats):
            start = time.perf_counter()
            dijkstra_result = dijkstra(graph, 0)
            dijkstra_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            bellman_result = bellman_ford(graph, 0)
            bellman_ford_times.append(time.perf_counter() - start)

        assert dijkstra_result == bellman_result, \
            "The algorithms produced different results!"

        dijkstra_avg = sum(dijkstra_times) / repeats
        bellman_avg = sum(bellman_ford_times) / repeats

        writer.writerow([
            size,
            dijkstra_avg,
            bellman_avg
        ])

        print(
            f"Vertices: {size} | "
            f"Dijkstra: {dijkstra_avg:.6f}s | "
            f"Bellman-Ford: {bellman_avg:.6f}s"
        )

print("\nResults saved to results.csv")