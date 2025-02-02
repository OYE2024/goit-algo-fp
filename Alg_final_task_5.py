import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, index=0):
    if index >= len(heap) or heap[index] is None:
        return None

    node = Node(heap[index])
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap, left_index)
    node.right = build_heap_tree(heap, right_index)

    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=node_colors)
    plt.show()


def generate_color(step, total_steps):
    base_color = [135, 206, 250]
    # Зміна кольору поступово від початку до кінця
    darken_factor = int((step / total_steps) * 255)
    new_color = [max(c - darken_factor, 0) for c in base_color]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Зміна кольору
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return colors


def bfs_visualize(root, total_steps=1):
    visited, queue = set(), [root]
    colors = {}
    step = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            # Зміна кольору
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return colors


heap = [1, 3, 5, 7, 9, 11, 13]

root = build_heap_tree(heap)

# Генерація кольорів для DFS та BFS
total_steps_dfs = len(heap)
total_steps_bfs = len(heap)

colors_dfs = dfs_visualize(root, total_steps_dfs)
colors_bfs = bfs_visualize(root, total_steps_bfs)

# Візуалізація DFS
draw_tree(root, colors_dfs)

# Візуалізація BFS
draw_tree(root, colors_bfs)
