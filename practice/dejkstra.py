# import heapq

from queue import PriorityQueue
import sys

vertex_distance = []
parent_vertexes = []


def dijkstra(graph: list, start_vertex: int):
    init_graph_vars(graph, start_vertex)

    # we need to have priority queue to store available nodes
    # and pickup the one with lowest weight
    # it stores the tuples (distance_to_it, vertex)
    # in such priority that vertex with lowest distance is on
    # position 0
    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0, start_vertex))

    # infinite cycle right now
    # available_vertexes_queue: (159, 5)
    while not available_vertexes_queue.empty():
        vertex_to_check = available_vertexes_queue.get()[1]

        for child_vertex_tuple in graph[vertex_to_check]:
            child_vertex = child_vertex_tuple[0]
            distance = vertex_distance[vertex_to_check] + child_vertex_tuple[1]
            if relax_edge(child_vertex, vertex_to_check, distance):
                available_vertexes_queue.put((distance, child_vertex))
        print(vertex_to_check)


def relax_edge(child_vertex, parent_vertex, distance):
    """
    stores the distance between two vertexes and parent one
    for the passed child
    """
    if vertex_distance[child_vertex] < distance:
        return False
    parent_vertexes[child_vertex] = parent_vertex
    vertex_distance[child_vertex] = distance
    return True


def init_graph_vars(graph: list, start_vertex: int):
    for vertex in graph:
        vertex_distance.append(sys.maxsize)
        parent_vertexes.append(None)
    vertex_distance[start_vertex] = 0

    # parent_vertexes[1] - 0 the vertex from which we come to v_1
    # parent_vertexes[0] - None
    # parent_vertexes[2] - 0
    # parent_vertexes[3] - 2
    # parent_vertexes[4] - 1
    # parent_vertexes[5] - 4


adjacency_list = [
    [(1, 99), (2, 50)],
    [(4, 50), (3, 50), (2, 50)],
    [(3, 99)],
    [(4, 75)],
    [(5, 10)],
]

dijkstra(adjacency_list, 0)

print(vertex_distance)

# -->
# 1 - 99
# 2 - 50
# 3 - 149
# 4 - 149
# 10 - 159


