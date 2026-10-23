# Shortest-Path Algorithm Comparison

## Overview
This project compares Dijkstra's algorithm and the Bellman-Ford algorithm for finding shortest paths in weighted graphs.

The algorithms are implemented in Python and evaluated using randomly generated, connected, undirected graphs with positive edge weights.

## Algorithms
- **Dijkstra's Algorithm:** Uses a priority queue to find shortest paths efficiently when edge weights are non-negative.
- **Bellman-Ford Algorithm:** Repeatedly relaxes edges and supports negative edge weights, provided there is no reachable negative-weight cycle.

## Features
- Random weighted graph generation
- Shortest-path implementations of both algorithms
- Execution-time benchmarking across different graph sizes
- CSV storage of benchmark results
- Performance visualization using Matplotlib
- Basic correctness tests

## Project Structure
```text
shortest-path-algorithm-comparison/
├── dijkstra.py
├── bellman_ford.py
├── graph_generator.py
├── benchmark.py
├── plot_results.py
├── test_algorithms.py
├── results.csv
├── performance_comparison.png
└── README.md
```

## Requirements
- Python 3
- Matplotlib

Install Matplotlib using:

```bash
pip install matplotlib
```

## How to Run

Run the correctness tests:

```bash
python test_algorithms.py
```

Generate benchmark results:

```bash
python benchmark.py
```

Plot the results:

```bash
python plot_results.py
```

## Experimental Results
The benchmark records the average execution time of each algorithm for different graph sizes. The results are saved in `results.csv` and visualized in `performance_comparison.png`.

In the current experiment, Dijkstra's algorithm runs faster than Bellman-Ford on the tested graphs. Actual timings depend on the hardware, graph structure, and system conditions.

## Technologies Used
- Python
- Data Structures and Algorithms
- Graph Theory
- Matplotlib
- CSV
- Git and GitHub