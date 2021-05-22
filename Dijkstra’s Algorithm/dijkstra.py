import math


def arg_min(T, S):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

V_num = len(D)  # число вершин в графе
T = [math.inf] * V_num   # последняя строка таблицы

vertex = 0       # стартовая вершина (нумерация с нуля)
S = {vertex}     # просмотренные вершины
T[vertex] = 0    # нулевой вес для стартовой вершины
M = [0] * V_num   # оптимальные связи между вершинами

while vertex != -1:          # цикл, пока не просмотрим все вершины
    for j, dw in enumerate(D[vertex]):   # перебираем все связанные вершины с вершиной v
        if j not in S:           # если вершина еще не просмотрена
            w = T[vertex] + dw
            if w < T[j]:
                T[j] = w
                M[j] = vertex        # связываем вершину j с вершиной v

    vertex = arg_min(T, S)            # выбираем следующий узел с наименьшим весом
    if vertex >= 0:                    # выбрана очередная вершина
        S.add(vertex)                 # добавляем новую вершину в рассмотрение

#print(T, M, sep="\n")

# формирование оптимального маршрута:
start = 0
end = 4
P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)

print(P)