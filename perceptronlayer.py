import perceptron


class Perceptronlayer:
    """The perceptron layer class. Contains a list of perceptron classes."""

    def __init__(self,  perceptrons):
        """Initializes all variables when the class is made.
        Contains the list of layers (a set of perceptrons) which is the network itself"""
        self.layer = []
        self.perceptron_amount = len(perceptrons)
        for i in perceptrons:
            self.layer.append(perceptron.Perceptron(i[0], i[1]))  # i[0] are the weights of each perceptron, i[1] are the biases

    def __str__(self):
        """Rerurns a string that tell the information of a whole layer
        Gives the bias and weights of each perceptron of the layer and
        shows which perceptron it is"""
        stri = ""
        count = 0
        for i in self.layer:
            count += 1
            stri += "Perceptron " + str(count) + ": " + str(i) + "\n"
        return stri


if __name__ == "__main__":
    a = Perceptronlayer([[[1, 2], 2],
                         [[1, 2], 3],
                         [[1, 2], 1],
                         [[1, 2], 2],
                         [[1, 2], 3]])
    print(a)
