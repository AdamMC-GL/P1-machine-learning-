
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
        self.output = False

    def activate(self, input):
        """Given the input this function calcualtes wether or not the perceptron
        should activate. Each weight with input True is summed up plus the bias,
        if this is greater than or equal to 0 the perceptron activates"""
        active_weights = [self.weights[i] for i in range(len(self.weights)) if input[i]]  # A list of all the weights where the input is True
        self.output = False
        if sum(active_weights) + self.bias >= 0:
            self.output = True
        return self.output

    def __str__(self):
        """Rerurns a string that tell the information of the perceptron
        Gives the bias and weights of the perceptron."""
        return "bias: " + str(self.bias) + ", weights: " + str(self.weights)


if __name__ == "__main__":
    input_combinations = [[False, False], [False, True], [True, False], [True, True]]

    invert = Perceptron([-0.5], 0)
    print("Invert: ")
    print(invert.activate([False]))
    print(invert.activate([True]))

    andport = Perceptron([0.5, 0.5], -1)
    print("AND: ")
    for i in input_combinations:
        print(andport.activate(i))

    orport = Perceptron([0.5, 0.5], -0.5)
    print("OR: ")
    for i in input_combinations:
        print(orport.activate(i))

    norport = Perceptron([-0.3, -0.3, -0.4], 0)
    print("NOR: ")
    input_combinations_3 = [[False, False, False], [False, True, True], [False, True, False], [True, True, True]]
    for i in input_combinations_3:
        print(norport.activate(i))

    three_input = Perceptron([0.6, 0.3, 0.2], -0.4)
    print("3 input example: ")
    for i in input_combinations_3:
        print(three_input.activate(i))
