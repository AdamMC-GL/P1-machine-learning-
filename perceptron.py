
class Perceptron:
    """The class of a perceptron, contains a set of weights and a bias.
    The function activate() dictates if the perceptron has a True or False output determined
    by its weights and bias."""

    def __init__(self, weights=None, bias=None):
        """Initializes all variables when the class is made.
        Contains the weights of the perceptron and its bias, the
        output of the perceptron always starts as false"""
        self.weights = weights
        self.bias = bias
        self.output = 0

    def activate(self, inputs):
        """Given the input this function calcualtes wether or not the perceptron
        should activate. Each weight with input True is summed up plus the bias,
        if this is greater than or equal to 0 the perceptron activates"""
        active_weights = [self.weights[i] * inputs[i] for i in range(len(self.weights))]  # A list of all the weights where the input is True
        self.output = 0
        if sum(active_weights) + self.bias >= 0:
            self.output = 1
        return self.output

    def __str__(self):
        """Rerurns a string that tell the information of the perceptron
        Gives the bias and weights of the perceptron."""
        return "bias: " + str(self.bias) + ", weights: " + str(self.weights)


if __name__ == "__main__":
    input_combinations = [[0, 0], [0, 1], [1, 0], [1, 1]]

    invert = Perceptron([-0.5], 0)
    print("Invert: ")
    print(invert.activate([0]))
    print(invert.activate([1]))
    assert invert.activate([0]) == 1, "Should be 1"
    assert invert.activate([1]) == 0, "Should be 0"

    andport = Perceptron([0.5, 0.5], -1)
    print("AND: ")
    for i in input_combinations:
        print(andport.activate(i))

    assert andport.activate([0, 0]) == 0, "Should be 0"
    assert andport.activate([0, 1]) == 0, "Should be 0"
    assert andport.activate([1, 0]) == 0, "Should be 0"
    assert andport.activate([1, 1]) == 1, "Should be 1"

    orport = Perceptron([0.5, 0.5], -0.5)
    print("OR: ")
    for i in input_combinations:
        print(orport.activate(i))

    assert orport.activate([0, 0]) == 0, "Should be 0"
    assert orport.activate([0, 1]) == 1, "Should be 1"
    assert orport.activate([1, 0]) == 1, "Should be 1"
    assert orport.activate([1, 1]) == 1, "Should be 1"

    norport = Perceptron([-0.3, -0.3, -0.4], 0)
    print("NOR: ")
    input_combinations_3 = [[0, 0, 0], [0, 1, 1], [0, 1, 0], [1, 1, 1]]
    for i in input_combinations_3:
        print(norport.activate(i))

    assert norport.activate([0, 0, 0]) == 1, "Should be 1"
    assert norport.activate([0, 1, 1]) == 0, "Should be 0"
    assert norport.activate([0, 1, 0]) == 0, "Should be 0"
    assert norport.activate([1, 1, 1]) == 0, "Should be 0"

    three_input = Perceptron([0.6, 0.3, 0.2], -0.4)
    print("3 input example: ")
    for i in input_combinations_3:
        print(three_input.activate(i))

    assert three_input.activate([0, 0, 0]) == 0, "Should be 0"
    assert three_input.activate([0, 1, 1]) == 1, "Should be 1"
    assert three_input.activate([0, 1, 0]) == 0, "Should be 0"
    assert three_input.activate([1, 1, 1]) == 1, "Should be 1"
