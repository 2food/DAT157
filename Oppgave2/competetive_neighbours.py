#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def main():
    file = open("KONKURR2.DAT", "r")

    patterns = []
    for line in file:
        if line[0].isdigit():
            pattern = [int(s) for s in line.rstrip().split(' ')]
            for _ in range(3):
                pattern += ([int(s) for s in file.readline().split(' ')])
            patterns.append(pattern)

    categories = 2
    alpha = 0.1
    iterations = 2000

    weights = []
    for _ in range(categories):
        w = [np.random.randint(0, 100) for _ in patterns[0]]
        s = sum(w)
        weights.append(list(map((lambda x: x / s), w)))

    print("Training with", iterations, "iterations and alpha:", alpha)

    for i in range(iterations):
        for p in patterns:
            weights = learn(alpha, p, weights, categories)

    check(patterns, weights, categories)


def show(edges):
    for i in range(16):
        if i % 4 == 0 and i != 0:
            print()
            for j in range(i - 4, i):
                if [j, j + 4] in edges:
                    print("|", end="   ")
                else:
                    print(" ", end="   ")
            print()
        print("¤", end=" ")
        if [i, i+1] in edges:
            print("-", end=" ")
        else:
            print(" ", end=" ")
    print()


def patterns2edges(patterns):
    edges = []
    for p in patterns:
        edges.append([i for i, x in enumerate(p) if x == 1])
    return edges


def compete(pattern, weights, size):
    sums = []
    for i in range(size):
        sums.append(sum([n * w for n, w in zip(pattern, weights[i])]))
    output = [1 if n == sums.index(max(sums)) else 0 for n in range(size)]
    return output


def learn(alpha, pattern, weights, size):
    output = compete(pattern, weights, size)
    for i in range(size):
        if output[i] == 1:
            dws = [alpha * (n / sum(pattern) - w) for n, w in zip(pattern, weights[i])]
            weights[i] = list(map(lambda x: x[0] + x[1], zip(weights[i], dws)))
    return weights


def check(patterns, weights, size):
    groups = [[] for _ in range(size)]
    for p in patterns:
        res = compete(p, weights, size)
        groups[res.index(1)].append(p)
    for i in range(len(groups)):
        print("Group:", i)
        edges = patterns2edges(groups[i])
        show(edges)
        print()


if __name__ == '__main__':
    main()
