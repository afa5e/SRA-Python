# Logic Gates
Logic gates are a visual representation of various boolean functions, allowing us to diagramatically design logic circuits. To simulate the circuits, we will be creating functions in python, taking in a list of inputs and returning a single output, or a list of outputs.
## Template:
[Template file](template.md)

## Example code:
```python
from itertools import product

# Define the number of inputs our simulation needs
NUMBER_OF_INPUTS = 2

# Defining our AND logic gate
def AND(inputs):
    if inputs[0] == True and inputs[1] == True:
        return True
    else:
        return False


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



# Simulate the AND gate
simulate(AND)
```

## Tasks:
### 1. Create functions for all of the following logic gates: AND, OR, NOT, NAND, NOR, XOR, XNOR.
#### AND
| Input | Input | Output |
|-------|-------|--------|
| 1     | 1     | 1      |
| 1     | 0     | 0      |
| 0     | 1     | 0      |
| 0     | 0     | 0      |


#### OR
| Input | Input | Output |
|-------|-------|--------|
| 1     | 1     | 1      |
| 1     | 0     | 1      |
| 0     | 1     | 1      |
| 0     | 0     | 0      |


#### NOT
| Input | Output |
|-------|--------|
| 1     | 0      |
| 0     | 1      |


#### NAND
| Input | Input | Output |
|-------|-------|--------|
| 1     | 1     | 0      |
| 1     | 0     | 1      |
| 0     | 1     | 1      |
| 0     | 0     | 1      |


#### NOR
| Input | Input | Output |
|-------|-------|--------|
| 1     | 1     | 1      |
| 1     | 0     | 0      |
| 0     | 1     | 0      |
| 0     | 0     | 0      |


#### XOR
| Input | Input | Output |
|-------|-------|--------|
| 1     | 1     | 0      |
| 1     | 0     | 1      |
| 0     | 1     | 1      |
| 0     | 0     | 0      |


#### XNOR
| Input | Input | Output |
|-------|-------|--------|
| 1     | 1     | 1      |
| 1     | 0     | 0      |
| 0     | 1     | 0      |
| 0     | 0     | 1      |

### 2. Create a half adder.
A half adder circuit takes in two binary numbers and sums them together, returning a sum and carry. This circuit will have two inputs and two outputs.
| Input | Input | Sum | Carry |
|-------|-------|-----|-------|
| 1     | 1     | 0   | 1     |
| 1     | 0     | 1   | 0     |
| 0     | 1     | 1   | 0     |
| 0     | 0     | 0   | 0     |

### Extension: Create all logic gates with only NAND gates 
##### Example: AND gate:
```python
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
```

### Extension: Create all logic gates with only NOR gates
