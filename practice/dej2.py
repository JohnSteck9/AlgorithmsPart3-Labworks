import pprint


def read_file(file_name: str):
    with open(file_name) as f:
        next(f)  # skip first line
        lines = f.readlines()
        index = 0
        graph = []
        counter = 2
        for line in lines:
            edge = []
            for num in line:
                arrow = 1
                try:
                    int(num)
                except:
                    continue
                index += 1
                vertex = (index, int(num))
                edge.append(vertex)
            graph.append(edge)
        print(graph)
    return graph


graph = read_file("carrer.in")

# graph = [
#     [(1, 3), (2, 5)],
#     [(3, 2), (4, 1), (5, 6)],
#     [(6, 7), (7, 3), (8, 2), (9, 4)]
# ]

def init_graph_vars(graph: list, start_vertex):
    vertex_distance = []
    parent_vertexes = []
