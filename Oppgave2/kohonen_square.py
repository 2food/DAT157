#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def main():
    size = 10

    nodes = []
    for y in range(size):
        line = []
        for x in range(size):
            line.append([0.5 + (x-5) / 1000, 0.5 - (y-5) / 1000])
        nodes.append(line)

    alpha = 0.2
    neighbours = 5
    iterations = 1000

    nodes = learn(alpha, neighbours, nodes, iterations)

    print("Final values:")
    show(nodes)


def show(nodes):
    xs, ys = [], []
    for row in nodes:
        for x, y in row:
            xs.append(x)
            ys.append(y)
    plt.plot(xs, ys, 'ro')
    plt.axis([0, 1, 0, 1])
    plt.show()


def winner(nodes, inn):
    x, y = inn
    minrow, mincol = 0, 0
    for row in range(len(nodes)):
        for col in range(len(nodes)):
            thisdiff = np.sqrt((x - nodes[row][col][0]) ** 2 + (y - nodes[row][col][1]) **2)
            mindiff = np.sqrt((x - nodes[minrow][mincol][0]) ** 2 + (y - nodes[minrow][mincol][1]) **2)
            if thisdiff < mindiff:
                minrow = row
                mincol = col
    return minrow, mincol


def learn(al0, neigh0, nodes, it):
    for i in range(it):
        al = al0 * (1-(i/it))
        neigh = np.ceil(neigh0 * (1-(i/it)))
        if i % 50 == 0:
            print("Iteration:", i)
            print("Alpha:", al, "Neighbour:", neigh)
            show(nodes)
        x, y = np.random.uniform(), np.random.uniform()
        winrow, wincol = winner(nodes, (x, y))
        for row in range(len(nodes)):
            if winrow - neigh <= row <= winrow + neigh:
                for col in range(len(nodes)):
                    if wincol - neigh <= col <= wincol + neigh:
                        nodes[row][col][0] += al * (x - nodes[row][col][0])
                        nodes[row][col][1] += al * (y - nodes[row][col][1])
    return nodes


if __name__ == '__main__':
    main()
