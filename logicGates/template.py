from itertools import product

###############################################################################
# Change this number to match the number of inputs                            # 
NUMBER_OF_INPUTS = 2                                                          #
###############################################################################

# Defining our AND logic gate
def AND(inputs):
    if inputs[0] == True and inputs[1] == True:
        return True
    else:
        return False

###############################################################################
# Add your code under this block                                              # ###############################################################################




###############################################################################
# Add your code above this block                                              # ###############################################################################

# Code to simulate all combinations, DO NOT CHANGE!
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

        # Iterates through the list of outputs
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

###############################################################################
# Change the name of the function inside "simulate" to the function           #
# you are testing                                                             # ###############################################################################

# Simulate the AND gate
simulate(AND)