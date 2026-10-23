import csv
import matplotlib.pyplot as plt

vertices = []
dijkstra_times = []
bellman_ford_times = []

with open("results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        vertices.append(int(row["vertices"]))
        dijkstra_times.append(float(row["dijkstra_time"]))
        bellman_ford_times.append(float(row["bellman_ford_time"]))

plt.plot(vertices, dijkstra_times, marker="o", label="Dijkstra")
plt.plot(vertices, bellman_ford_times, marker="o", label="Bellman-Ford")

plt.xlabel("Number of vertices")
plt.ylabel("Average execution time (seconds)")
plt.title("Shortest-Path Algorithm Performance Comparison")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("performance_comparison.png", dpi=300)
plt.show()