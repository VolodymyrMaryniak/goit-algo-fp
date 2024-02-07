import networkx as nx
import matplotlib.pyplot as plt
import heapq
import random


def dijkstra(graph: nx.Graph, start):
    distances = {
        node: 0 if node == start else float("infinity") for node in graph.nodes()
    }

    predecessors = {node: None for node in graph.nodes()}
    unvisited_heap = [(0, start)]

    while unvisited_heap:
        current_distance, current_node = heapq.heappop(unvisited_heap)

        if current_distance > distances[current_node]:
            continue

        neighbors = graph.neighbors(current_node)
        for neighbor in neighbors:
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                heapq.heappush(unvisited_heap, (distance, neighbor))

                distances[neighbor] = distance
                predecessors[neighbor] = current_node
    result = {
        node: (distances[node], get_shortest_path(predecessors, node))
        for node in graph.nodes()
    }
    return result


def get_shortest_path(predecessors, end):
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    return path


def show_graph(graph):
    pos = nx.kamada_kawai_layout(graph)

    edge_labels = nx.get_edge_attributes(graph, "weight")

    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_size=8,
        edge_color="gray",
    )

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.show()


def create_graph():
    graph = nx.Graph()
    graph.add_edges_from(
        [
            ("A", "B", {"weight": 12}),
            ("A", "C", {"weight": 15}),
            ("A", "E", {"weight": 50}),
            ("A", "I", {"weight": 68}),
            ("B", "C", {"weight": 20}),
            ("B", "D", {"weight": 25}),
            ("C", "D", {"weight": 30}),
            ("D", "E", {"weight": 41}),
            ("D", "G", {"weight": 20}),
            ("E", "F", {"weight": 35}),
            ("E", "H", {"weight": 21}),
            ("E", "I", {"weight": 31}),
            ("F", "G", {"weight": 32}),
        ]
    )

    return graph


def main():
    graph = create_graph()

    start = "A"
    results = dijkstra(graph, start)
    for end, (distance, path) in results.items():
        print(f"{start} -> {end}: {path} ({distance})")

    show_graph(graph)


if __name__ == "__main__":
    main()
