import heapq
import networkx as nx
import matplotlib.pyplot as plt

# створення графа
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'D', weight=3)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'D', weight=5)

# Алгоритм Дейкстри


def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


# Запуск алгоритма
start_node = 'A'
shortest_paths = dijkstra(G, start_node)
print("Кратчайшие расстояния:", shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        edge_color='gray', node_size=2000, font_size=16)

# відображення ваг ребер
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.show()
