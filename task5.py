import uuid
import heapq
import random
import typing

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title: str = None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }
    
    fig = plt.figure(figsize=(8, 5))
    if title:
        fig.suptitle(title)

    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )

    plt.show()


def build_binary_tree_from_heap(heap, node_index=0):
    if node_index >= len(heap):
        return None

    root = Node(heap[node_index])

    left_index = 2 * node_index + 1
    right_index = 2 * node_index + 2

    root.left = build_binary_tree_from_heap(heap, left_index)
    root.right = build_binary_tree_from_heap(heap, right_index)
    return root


def draw_binary_heap(heap):
    root = build_binary_tree_from_heap(heap)
    draw_tree(root)


def generate_colors(num_colors):
    colors = []
    for i in range(num_colors):
        # Генеруємо компоненти RGB
        r = int((i / num_colors) * 255)
        g = int((i / num_colors) * 255)
        b = int((i / num_colors) * 255)
        color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
        colors.append(color_hex)
    return colors


def dfs_recursive(
    node: Node,
    visit_callback: typing.Callable[[Node, int], None] = None,
    params: dict = None,
):
    if params is None:
        params = {"index": 0}
    else:
        params["index"] += 1

    # Visit the Node
    if visit_callback is not None:
        visit_callback(node, params["index"])

    if node.left:
        dfs_recursive(node.left, visit_callback, params)

    if node.right:
        dfs_recursive(node.right, visit_callback, params)


def bfs_recursive(
    queue: typing.Deque,
    visit_callback: typing.Callable[[Node, int], None] = None,
    params: dict = None,
):
    if not queue:
        return

    if params is None:
        params = {"index": 0}
    else:
        params["index"] += 1

    node = queue.popleft()

    # Visit the Node
    if visit_callback is not None:
        visit_callback(node, params["index"])

    if node.left:
        queue.append(node.left)

    if node.right:
        queue.append(node.right)

    bfs_recursive(queue, visit_callback, params)


def main():
    count_of_nodes = 10
    heap = [random.randint(0, 100) for _ in range(count_of_nodes)]
    heapq.heapify(heap)

    root = build_binary_tree_from_heap(heap)
    colors = generate_colors(count_of_nodes)

    # Breadth-first search
    bfs_recursive(
        queue=deque([root]),
        visit_callback=lambda node, index: setattr(node, "color", colors[index]),
    )

    draw_tree(root, title="Breadth-first search")

    # Depth-first search
    dfs_recursive(
        root, visit_callback=lambda node, index: setattr(node, "color", colors[index])
    )

    draw_tree(root, title="Depth-first search")


if __name__ == "__main__":
    main()
