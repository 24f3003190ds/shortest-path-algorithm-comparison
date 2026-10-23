from dijkstra import dijkstra
from bellman_ford import bellman_ford


def test_shortest_paths():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8)],
        "D": [("B", 5), ("C", 8)]
    }

    expected = {
        "A": 0,
        "B": 3,
        "C": 2,
        "D": 8
    }

    assert dijkstra(graph, "A") == expected
    assert bellman_ford(graph, "A") == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_shortest_paths()