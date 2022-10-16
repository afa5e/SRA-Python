print("Number in base 7: ", end = "")
baseSeven = input()
column = len(baseSeven)
i = 0
baseTen = 0

for digit in baseSeven:
    baseTen += int(baseSeven[i:i + 1]) * 7 ^ (column - i - 1)
    print(column - i)
    i += x1

print(baseTen)