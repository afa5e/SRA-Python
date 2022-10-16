print("Input number: ", end = "")
number = input()

even = []
odd = []
mask = []
output = ""

for digit in number:
    if int(digit) % 2 == 0:
        mask.append("e")
        even.append(int(digit))
    else:
        mask.append("o")
        odd.append(int(digit))

even.sort(reverse = True)
odd.sort(reverse = True)

for digit in mask:
    if digit == "e":
         output += str(even[0])
         even.pop(0)
    else:
        output += str(odd[0])
        odd.pop(0)

print("The greatest number after swapping equal parity digis is" , output)
