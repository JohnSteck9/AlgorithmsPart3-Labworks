from typing import List, Tuple


class Company:
    def __init__(self):
        self.layers = 0
        self.graph: List[Tuple[int, ...]] = []

    # def read_file(self, file_name: str):
    #     try:
    #         with open(file_name) as f:
    #             # next(f)  # skip first line
    #             lines = f.readlines()
    #             for line in lines:
    #                 line = tuple(map(int, line.split()))
    #                 if len(line) > 2:
    #                     Company.generate_graph_tree(line, self.graph)
    #                 else:
    #                     self.graph.append(line)
    #                 self.layers += 1
    #             print(self.graph)
    #
    #     except FileNotFoundError as error:
    #         print("!", error), exit()
    #     except ValueError as error:
    #         print(f"Value Error in file: {file_name}\n", error, end=""), exit()
    #
    # @staticmethod
    # def generate_graph_tree(line, graph):
    #     index = 0
    #     while index+2 <= len(line):
    #         graph.append((line[index], line[index+1]))
    #         index += 1


    def read_file(self, file_name: str):
        try:
            with open(file_name) as f:
                # next(f)  # skip first line
                lines = f.readlines()
                for line in lines:
                    line = list(map(int, line.split()))
                    print(line)
                    self.graph.extend(line)
                    self.layers += 1
                print(self.graph)

        except FileNotFoundError as error:
            print("!", error), exit()
        except ValueError as error:
            print(f"Value Error in file: {file_name}\n", error, end=""), exit()


    def solution(self):
        visited = [False for _ in self.graph]
        experience = [0 for x in self.graph]
        max_value = 0
        row = []
        while self.layers > 0:








class Node:

    def __init__(self, data, father=None, left_child=None, right_child=None):
        self.father = father
        self.left_child = left_child
        self.right_child = right_child
        self.data = data


    def print_node(self):
        pass


if __name__ == '__main__':
    company = Company()
    company.read_file("carrer.in")
    #company.solution()
    # print(solution(graph))