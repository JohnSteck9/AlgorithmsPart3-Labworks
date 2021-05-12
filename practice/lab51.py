from math import sin, pi
import matplotlib.pylab as plt

U_max = 100
frequency = 50
R1 = 5
R2 = 4
R3 = 7

L1 = 0.01
C1 = 300 * 10 ** -6
C2 = 150 * 10 ** -6


func = [lambda current_time, X: ((U_max * sin(2 * pi * frequency * current_time) - X[0] + (X[1] * R3) - (X[2]))
                             / (R1 + R3) / C1),
     lambda current_time, X: (((U_max * sin(2 * pi * frequency * current_time) - X[0] + (X[1] * R3) - (X[2]))
                           / (R1 + R3)) * R1 / L1),
     lambda current_time, X: (((U_max * sin(2 * pi * frequency * current_time) - X[0] + (X[1] * R3) - (X[2]))
                           / (R1 + R3)) * R3 / C2)]


def output_voltage(value):
    return value[2]


def get_next_value(current_time, next_cur_time, value, h):
    next_value = value

    for i in range(len(value)):
        next_value[i] = value[i] + h * func[i](current_time, value)

    return next_value


def get_results(current_time, time_end, value, h):
    time_value = dict()

    while current_time < time_end:
        next_cur_time = current_time + h
        next_value = get_next_value(current_time, next_cur_time, value, h)

        current_time = next_cur_time
        value = next_value

        time_value[current_time] = output_voltage(value)

    return time_value


if __name__ == '__main__':
    current_time = 0
    value = [0, 0, 0]
    time_end = 0.2
    h = 0.00001

    time_value = get_results(current_time, time_end, value, h)

    current_times = []
    values = []
    for t, v in time_value.items():
        current_times.append(t)
        values.append(v)

    plt.plot(current_times, values)
    plt.show()
