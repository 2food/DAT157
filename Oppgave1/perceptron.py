import numpy as np
import matplotlib.pyplot as pyplot


def initialValues():
    return [[1, 0, 0], [0]]


def initialWeigths():
    return [np.random.random(), np.random.random(), np.random.random()]


def setInput(inputs):
    global values
    values[0][1] = inputs[0]
    values[0][2] = inputs[1]


def sigmoidal(sum):
    return 1 / (1 + np.exp(-sum))


def compute(x, y):
    global values
    global weights
    setInput([x, y])
    vw = [v*w for (v, w) in zip(values[0], weights)]
    if (sum(vw)) > 0:
        values[1][0] = 1
    else:
        values[1][0] = 0
    return values[1][0]


def train(iterations):
    global values
    global weights
    global alpha
    global rms
    sum_of_errors = 0
    for i in range(iterations):
        x, y = np.random.randint(0, 2), np.random.randint(0, 2)
        t = op(x, y)
        a = compute(x, y)
        sum_of_errors += ((t-a) ** 2)
        rms.append(np.sqrt(sum_of_errors / (i+1)))
        if t != a:
            new_weights = []
            for (v, w) in zip(values[0], weights):
                new_weights.append(w + alpha * (t-a) * v)
            weights = new_weights


def test():
    print("(0, 0) ->", compute(0, 0))
    print("(0, 1) ->", compute(0, 1))
    print("(1, 0) ->", compute(1, 0))
    print("(1, 1) ->", compute(1, 1))


if __name__ == '__main__':
    values = initialValues()
    weights = initialWeigths()
    alpha = 0.1
    rms = []

    operators = {"and": (lambda x, y: x and y),
                 "or": (lambda x, y: x or y),
                 "xor": (lambda x, y: x != y)}

    op = operators[input("and / or / xor: ")]

    iterations = int(input("Number of iterations: "))

    train(iterations)

    pyplot.plot(rms)
    pyplot.show()
    test()
