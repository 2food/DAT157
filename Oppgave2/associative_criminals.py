#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# Criminals:
# Harald [1,1,0,0] - Blåøyd, Blond, 1.90, venstrehendt, 30-40, vestlandsk, mann
# [0,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0]
# Vigdis [0,0,1,1] - Grønnøyd, Svart, 1.60, høyrehendt, under 20, nordlandsk, kvinne


def main():
    ats = {"blå": [0, 0], "grønne": [0, 1], "brune": [1, 0], "grå": [1, 1],
           "blondt": [0, 0], "brunt": [0, 1], "svart": [1, 0], "rødt": [1, 1],
           "1.60": [0, 0], "1.70": [0, 1], "1.80": [1, 0], "1.90": [1, 1],
           "høyre": [0], "venstre": [1],
           "under 20": [0, 0], "20-30": [0, 1], "30-40": [1, 0], "over 40": [1, 1],
           "nordlandsk": [0, 0], "vestlandsk": [0, 1], "sørlandsk": [1, 0], "østlandsk": [1, 1],
           "mann": [0], "kvinne": [1]}

    file = open("criminals.txt", "r")
    names = []
    patterns = []
    for line in file:
        names.append(line)
        patterns.append([int(s) for s in file.readline().split(',')])

    size = len(patterns[0])
    nodes = [0 for _ in range(size)]
    weights = [[0 for _ in range(size)] for m in range(size)]

    weights = learn(size, weights, patterns)
    print(weights)
    # print("Har du sett an kriminell? Skriv inn det du så: (hvis du ikke vet sikkert så bare tipp)")
    # obs = get_obs(ats)
    # inn = []
    # for o in obs:
    #     inn += ats[o]
    inn = patterns[0][:]
    nodes[:len(inn)] = inn

    for _ in range(500):
        nodes = associate(nodes, weights)

    for n, p in zip(names, patterns):
        print("A criminal:", n)
        print("Pattern:", p, "\n")

    found = False
    for i in range(len(patterns)):
        if patterns[i] == nodes:
            print("The network chooses:", names[patterns.index(nodes)])
            found = True
    if not found:
        print("The network did not converge on a criminal")
    print("Pattern:", nodes)


def associate(nodes, weights):
    # går igjennom listen i tilfeldig rekkefølge
    for i in sorted(range(len(nodes)), key=lambda k: np.random.random()):
        if sum([n * w for (n, w) in zip(nodes, weights[i])]) >= 0:
            nodes[i] = 1
        else:
            nodes[i] = 0
    return nodes


def learn(size, weights, patterns):
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
