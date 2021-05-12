#         1
#    2        3
# 4   5       6
#           7   8

# BFS - Breadth First Search


def bfs(graph: list, start_vertex: int):
    visited = [False for x in graph]
    distances = [0 for x in graph]
    vertex_to_visit_queue = []
    vertex_to_visit_queue.append((start_vertex))
    while vertex_to_visit_queue:
        current_vertex = vertex_to_visit_queue.pop(0)

        # calculate distances
        for neighbour in graph[current_vertex]:
            # if visited vertex is black - ignore it
            if visited[current_vertex]:
                continue
            if visited[neighbour]:
                continue

            distances[neighbour] = distances[current_vertex] + 1

            # mark child vertex as grey
            vertex_to_visit_queue.append(neighbour)

        # mark vertex as black
        visited[current_vertex] = True
    return distances


if __name__ == '__main__':
    graph = [[1], [2, 3], [1, 4, 5], [1, 6], [2], [2], [3, 7, 8], [6], [6]]
    print(bfs(graph, 0))