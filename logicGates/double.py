
from itertools import product

# Define the number of inputs our simulation needs
NUMBER_OF_INPUTS = 4


# Defining our AND logic gate
def NOR(inputs):
    if inputs[0] == True or inputs[1] == True:
        return False
    else:
        return True

# AND gate from only NAND gates
def AND(inputs):
    if inputs[0] == True and inputs[1] == True:
        return True
    else:
        return False

def threeWayOR(inputs):
    if inputs[0] == True or inputs[1] == True or inputs[2] == True:
        return True
    else:
        return False

def double(inputs):
    stageTop = AND([inputs[0], inputs[1]])
    stageBottom = AND([inputs[2], inputs[3]])

    stageTopMid = NOR([inputs[0], inputs[1]])
    stageBottomMid = NOR([inputs[2], inputs[3]])

    stageMid = NOR([stageTopMid, stageBottomMid])

    output = threeWayOR([stageTop, stageMid, stageBottom])

    return output

# Code to simulate all combinations
def simulate(inputFunction):
    combinationList = product([True, False], repeat=NUMBER_OF_INPUTS)
    for inputOption in combinationList:
        i = 0

        # Print out the inputs and output
        for inputValue in inputOption:
            if i != len(inputOption) - 1:
                print(inputValue, end=", ")
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
simulate(double)
