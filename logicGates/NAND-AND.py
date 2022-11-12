from itertools import product

# Define the number of inputs our simulation needs
NUMBER_OF_INPUTS = 2


# Defining our AND logic gate
def NAND(inputs):
    if inputs[0] == True and inputs[1] == True:
        return False
    else:
        return True

# AND gate from only NAND gates
def AND(inputs):
    stageUpper = NAND(inputs)
    stageLower = NAND(inputs)

    output = NAND([stageUpper, stageLower])

    return output

# Code to simulate all combinations
def simulate(inputFunction):
    combinationList = product([True, False], repeat=NUMBER_OF_INPUTS)
    for inputOption in combinationList:
        i = 0

        # Print out the inputs and output
        for inputValue in inputOption:
            if i != len(inputOption) - 1:
                print(inputValue, end=" " + inputFunction.__name__ + " ")
            else:
                print(inputValue, end=": ")
            i += 1

        outputs = inputFunction(inputOption)
        i = 0
        if type(outputs) != bool:
            for outputValue in outputs:
                if i < len(outputs) - 1:
                    print(outputValue, end=", ")
                else:
                    print(outputValue)
                i += 1
        else:
            print(outputs)


# Simulate the AND gate
simulate(AND)
