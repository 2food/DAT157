#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def main():
    letters = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
                0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
                0, 1, 1, 0, 0, 0, 0, 1, 1, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
                1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
                0, 1, 1, 0, 0, 0, 0, 1, 1, 0,
                0, 0, 1, 1, 0, 0, 1, 1, 0, 0,
                0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
               [1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
                1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
                1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
                1, 1, 0, 1, 1, 0, 0, 0, 1, 1,
                1, 1, 0, 0, 1, 1, 0, 0, 1, 1,
                1, 1, 0, 0, 0, 1, 1, 0, 1, 1,
                1, 1, 0, 0, 0, 0, 1, 1, 1, 1,
                1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
                1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
                1, 1, 0, 0, 0, 0, 0, 0, 1, 1]]

    size = len(letters[0])
    weights = [[0 for _ in range(size)] for m in range(size)]

    weights = learn(weights, letters)

    nodes = add_noise(letters[1][:], 0.1)
    nodes = associate(nodes, weights)
    show_pattern(nodes)


def add_noise(pattern, degree):
    # TODO implement this
    return pattern


def show_pattern(pattern):
    for i in range(len(pattern)):
        if i % 10 == 0:
            print()
        print(pattern[i], end=" ")


def associate(nodes, weights):
    # går igjennom listen i tilfeldig rekkefølge
    for i in sorted(range(len(nodes)), key=lambda k: np.random.random()):
        if sum([n * w for (n, w) in zip(nodes, weights[i])]) >= 0:
            nodes[i] = 1
        else:
            nodes[i] = 0
    return nodes


def learn(weights, patterns):
    for p in patterns:
        for i in range(len(p)):
            for j in range(len(p)):
                if i != j:
                    weights[i][j] += (2 * p[i] - 1) * (2 * p[j] - 1)
    return weights


def get_obs(ats):
    prompts = ["Øyefarge (blå/grønne/brune/grå): ",
               "Hårfarge (blondt/brunt/svart/rødt): ",
               "Høyde (1.60/1.70/1.80/1.90): ",
               "Høyre- eller venstrehendt? (høyre/venstre): ",
               "Alder (under 20/20-30/30-40/over 40): ",
               "Dialekt (nordlandsk/vestlandsk/sørlandsk/østlandsk): ",
               "Kjønn (mann/kvinne): "]
    obs = []
    for p in prompts:
        obs.append(input(p))
        while not obs[-1] in ats:
            print("Wrong input! Try again.")
            obs[-1] = input(p)
    return obs


if __name__ == '__main__':
    main()
