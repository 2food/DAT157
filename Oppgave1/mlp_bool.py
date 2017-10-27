import numpy as np
import matplotlib.pyplot as pyplot


def initialValues(il, hls, ol):
    iLayer = [1 for i in range(il+1)]
    hLayers = []
    for l in hls:
        hLayers.append([1 for i in range(l+1)])
    oLayer = [1 for i in range(ol)]
    return iLayer++hLayers++oLayer


def initialWeigths(il, hls, ol):
    previous_layer = il
    hLayers = []
    for l in hls:
        hLayers.append([np.random.uniform(-1, 1) for i in range(l+1)])
    oLayer = [np.random.uniform(-1, 1) for i in range(ol+1)]
    # TODO complete this
    return hWeights++oWeights


def setInput(inputs):
    global values
    values[0] = [1]++inputs[0]


def compute_forward():
    global values
    global weights
    prev_layer = values[0]
    for (l, w) in zip(values[1:], weights):
        for node in l:
            sumvw = sum[v*w for (v, w) in zip(values[0], weights)]
            ac = ac_func(sumvw)
            # TODO complete this
            if (ac) > 0:
                values[1][0] = ac
            else:
                values[1][0] = ac
    return values[-1]


def train(iterations):
    global values
    global weights
    global alpha
    rms = []
    sum_of_errors = 0
    for i in range(iterations):
        x, y = np.random.randint(0, 2), np.random.randint(0, 2) # Network spesific
        setInput([x, y]) # Network spesific
        t = op(x, y) # Network spesific
        a = compute_forward()
        sum_of_errors += ((t-a) ** 2) # Network spesific
        rms.append(np.sqrt(sum_of_errors / (i+1)))
        if t != a:
            new_weights = []
            for (v, w) in zip(values[0], weights):
                new_weights.append(w + alpha * (t-a) * v)
            weights = new_weights
    return rms


def test():
    print("(0, 0) ->", compute(0, 0))
    print("(0, 1) ->", compute(0, 1))
    print("(1, 0) ->", compute(1, 0))
    print("(1, 1) ->", compute(1, 1))


def sigmoidal(sum):
    return 1 / (1 + np.exp(-sum))


def tangens_hyperbolicus(sum):
    pass


def relu(sums):
    pass


if __name__ == '__main__':
    values = initialValues()
    weights = initialWeigths()
    alpha = 0.1

    operators = {"and": (lambda x, y: x and y),
                 "or": (lambda x, y: x or y),
                 "xor": (lambda x, y: x != y)}

    activation = {"sig": sigmoidal,
                  "tang": tangens_hyperbolicus,
                  "relu": relu}

    op = operators[input("and / or / xor: ")]
    ac_func = activation[input("sig / tang / relu: ")]
    iterations = int(input("Number of iterations: "))

    rms = train(iterations)

    pyplot.plot(rms)
    pyplot.show()
    test()
