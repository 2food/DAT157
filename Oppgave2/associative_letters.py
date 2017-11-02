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

    names = ["T", "O", "N"]

    size = len(letters[0])
    weights = [[0 for _ in range(size)] for m in range(size)]

    weights = learn(weights, letters)

    T, O, N = 0, 1, 2
    nodes = add_noise(letters[T][:], 10)

    show_pattern(nodes)

    nodes = associate(100, nodes, weights)

    show_pattern(nodes)

    found = False
    for i in range(len(letters)):
        if nodes == letters[i]:
            found = True
            print("Output matches ", names[i], "!", sep="")

    if not found:
        print("Output does not match any letter!")


def add_noise(pattern, degree):
    indexes = np.random.randint(0, len(pattern), size=degree)
    for i in indexes:
        if pattern[i] == 1:
            pattern[i] = 0
        else:
            pattern[i] = 1
    return pattern


def show_pattern(pattern):
    for i in range(len(pattern)):
        if i % 10 == 0:
            print()
        print(pattern[i], end=" ")
    print()


def associate(iterations, nodes, weights):
    # går igjennom listen i tilfeldig rekkefølge
    for _ in range(iterations):
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
