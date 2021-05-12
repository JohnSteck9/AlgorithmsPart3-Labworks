from math import sin, pi
import matplotlib.pyplot as plt
from functools import lru_cache
import numpy as np
from time import time

a = 0.002
C1 = 4.8
C2 = 48
C3 = 7
R1 = 4
R2 = 43
R3 = 17
R4 = 30


final_time = 0.2
step = 0.000001


def U1_f(t):
    period = 6 * a
    while t > period:
        t -= period
    if t <= a:
        U1 = t * 10/a
    if a < t <= 2 * a:
        U1 = 10
    if 2 * a < t <= 3 * a:
        U1 = -(t * 10/a) + 30
    if 3 * a < t <= 6 * a:
        U1 = 0
    return U1


equations = [
    lambda X, t: (-((U1_f(t) * R2 + X[1]*R1 + X[2]*R1 - X[0]*R2) / (R1*R3 + R2*R3 + R1*R2))*R3+X[0]-U1_f(t))/(R1*C1),
    lambda X, t: -((U1_f(t) * R2 + X[1]*R1 + X[2]*R1 - X[0]*R2) / (R1*R3 + R2*R3 + R1*R2))+(-((U1_f(t) * R2 + X[1]*R1 + X[2]*R1 - X[0]*R2) / (R1*R3 + R2*R3 + R1*R2))*R3+X[0]-U1_f(t))/R1,
    lambda X, t: (-((U1_f(t) * R2 + X[1]*R1 + X[2]*R1 - X[0]*R2) / (R1*R3 + R2*R3 + R1*R2))+(-((U1_f(t) * R2 + X[1]*R1 + X[2]*R1 - X[0]*R2) / (R1*R3 + R2*R3 + R1*R2))*R3+X[0]-U1_f(t))/R1)-X[2]/R4
    ]

current_time = 0
result = []
times = []
previous = [0, 0, 0]
result.append(U1_f(0))
U1 = []
U2 = []
UC1 = []
UC2 = []
UC3 = []
start_time = time()
end_time = time()


def find_plot():
    global current_time
    global result
    global previous
    global U1
    global U2
    global UC1
    global UC2
    global UC3
    global start_time
    X = [0, 0, 0]
    while current_time < final_time:
        previous = []
        for i in range(len(X)):
            previous.append(X[i] + step * equations[i](X, current_time))
        for i in range(len(X)):
            X[i] += step * equations[i](previous, current_time)
        result.append(X[1])
        U1.append(U1_f(current_time))
        UC1.append(X[0])
        UC2.append(X[1])
        UC3.append(X[2])
        U2.append(X[2])
        times.append(current_time)
        current_time += step


if __name__ == '__main__':
    find_plot()
    plt.figure(1)
    plt.plot(times, U1)
    plt.xlabel('t')
    plt.ylabel('U1')

    plt.figure(2)
    plt.plot(times, UC1)
    plt.xlabel('t')
    plt.ylabel('UC1')

    plt.figure(3)
    plt.plot(times, UC2)
    plt.xlabel('t')
    plt.ylabel('UC2')

    plt.figure(4)
    plt.plot(times, UC3)
    plt.xlabel('t')
    plt.ylabel('UC3')

    plt.figure(5)
    plt.plot(times, U2)
    plt.xlabel('t')
    plt.ylabel('U2')

    plt.show()
    print(f"{time() - start_time}s")
