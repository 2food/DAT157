#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# Hamming-matrise for inputmøstre:
# P1 = (1 0 1), P2 = (1 0 0), P3 = (0 1 0), P4 = (0 1 1)
#       P1  P2  P3  P4
#   P1   0   1   3   2
#   P2   1   0   2   3
#   P3   3   2   0   1
#   P4   2   3   1   0
# Vi ser at vi kan dele inn i 2 grupper der mønstrene har Hamming-avstand 1 innad i gruppen:
# A = {P1, P2} og B = {P3, P4}

# Det konkurrerende nettverket finner samme inndeling som oss de fleste gangene.
# Den finner innimellom også denne inndelingen: A = {P1, P4} og B = {P3, P3}
# Vi ser i hamming-matrisen at dette er den nest beste løsningen siden begge gruppene da har avstand 2.


def main():
    patterns = [[1, 0, 1],
                [1, 0, 0],
                [0, 1, 0],
                [0, 1, 1]]

    outputlayer = [0, 0]
    size = len(outputlayer)
    alpha = 0.1
    iterations = 1000

    weights = []
    for _ in outputlayer:
        w = [np.random.randint(0, 100) for _ in patterns[0]]
        s = sum(w)
        weights.append(list(map((lambda x: x/s), w)))

    for i in range(iterations):
        weights = learn(alpha, patterns[i % 4], weights, size)

    print("Training with", iterations, "iterations and alpha:", alpha)
    check(patterns, weights, size)


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
    for p in patterns:
        print("Input:", p, "->", compete(p, weights, size))


if __name__ == '__main__':
    main()
