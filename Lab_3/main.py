class Career:
    def __init__(self):
        self.layers_num = 0
        self.layers_list = []

    def read_file(self, filename):
        with open(filename, 'r') as f:
            self.layers_num = int(f.readline())
            for line in f:
                self.layers_list.append(list(map(lambda x: int(x), line.split())))
        print(self.layers_list)

    @staticmethod
    def write_file(filename: str, text: str):
        f = open(filename, "w")
        f.write(text)
        f.close()

    def find_bigger(self, layer_index: int, position_index: int):
        left_position = self.layers_list[layer_index + 1][position_index]
        right_position = self.layers_list[layer_index + 1][position_index + 1]

        if left_position > right_position:
            self.layers_list[layer_index][position_index] += left_position
        else:
            self.layers_list[layer_index][position_index] += right_position

    def find_max_experience(self):
        for layer_index in range(self.layers_num - 2, -1, -1):
            for position_index in range(layer_index + 1):
                self.find_bigger(layer_index, position_index)
        return self.layers_list[0][0]


if __name__ == '__main__':
    FILE_IN = 'career.in'
    FILE_OUT = 'career.out'

    career = Career()
    career.read_file(FILE_IN)
    max_experience = career.find_max_experience()
    print(max_experience)
    career.write_file(FILE_OUT, str(max_experience))

