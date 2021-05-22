def read_file(filename: str):
    rows = []
    idx = 1

    with open(filename, 'r') as f:
        data = f.readline().split()  # ['3', '3']
        rows_num, columns_num = int(data[0]), int(data[1])

        for line in f:
            string_list = []
            for char in line:
                if char.split():
                    string_list.append(char + str(idx))
                    idx += 1

            rows.append(string_list)
            # print(rows)
    exit1, exit2 = rows[0][-1], rows[-1][-1]
    # transform rows to columns
    columns = list(map(list, zip(*rows)))

    return columns, rows_num, columns_num, exit1, exit2


def write_file(filename: str, text: str):
    with open(filename, 'w') as f:
        f.write(text)


def generate_graph(columns: list[list]):
    graph = {}

    for i in range(len(columns)):
        for j in range(len(columns[i])):
            # print(columns[i][j])
            try:
                edges_list = [columns[i + 1][j]]
            except IndexError:
                graph[columns[i][j]] = {}
                continue

            prefix1 = [columns[i][j]][0][:1]
            idx = i
            while idx + 1 < len(columns):
                # print(columns[idx])
                for k in columns[idx + 1]:
                    prefix2 = k[:1]
                    if prefix1 == prefix2:
                        # print(k)
                        edges_list.append(k)
                graph[columns[i][j]] = set(edges_list)
                idx += 1
    return graph


# Find a path from start to end
def find_path(graph: dict, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


# Find all the paths from start to end
def find_all_path(graph: dict, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []  # Store all paths
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_path(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


# Find the shortest path
def find_shortest_path(graph: dict, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    shortest_path = []
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path


def main(input_file: str, output_file: str = 'out.txt'):
    columns, rows_num, columns_num, exit1, exit2 = read_file(input_file)
    graph = generate_graph(columns)
    # print(graph)
    all_path_sum = 0

    if exit1 == exit2:
        all_path_sum = len(find_all_path(graph, columns[0][0], exit1))
        # write_file(output_file, str(all_path_sum))
        return all_path_sum

    for i in range(len(columns[0])):
        all_path_exit1 = find_all_path(graph, columns[0][i], exit1)
        # print('\nAll paths to exit 1:', all_path_exit1)
        all_path_exit2 = find_all_path(graph, columns[0][i], exit2)
        # print('All paths to exit 2:', all_path_exit2)
        all_path_sum += len(all_path_exit1) + len(all_path_exit2)

    # write_file(output_file, str(all_path_sum))
    return all_path_sum


if __name__ == '__main__':
    FILE_IN_1 = 'data/ijones1.in'
    FILE_OUT_1 = 'data/ijones1.out'

    FILE_IN_2 = 'data/ijones2.in'
    FILE_OUT_2 = 'data/ijones2.out'

    FILE_IN_3 = 'data/ijones3.in'
    FILE_OUT_3 = 'data/ijones3.out'

    all_path = main(FILE_IN_1)
    print(all_path)

    '''
adjacency_list_view = {
    'a1': {'a3', 'a5', 'a2'},
    'c4': {'a5'},
    'd7': {'e8'},
    'a2': {'a3'},
    'a5': {'b6', 'a3'},
    'e8': {'f9'},
    'a3': {},
    'b6': {},
    'f9': {}
}    
    
    '''

    # one_path = find_path(graph, 'a1', 'a3')
    # print('One path:', one_path)

    # all_path = find_all_path(graph, 'a1', 'a3')
    # print('\nAll paths:', all_path)
