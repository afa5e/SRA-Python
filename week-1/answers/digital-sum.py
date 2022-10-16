print("input number: ", end = "")
number = input()
total = 0

while int(number) >= 10:
    for digit in number:
        total += int(digit)

    number = str(total)
    total = 0

print("The digital sum is", int(number))
