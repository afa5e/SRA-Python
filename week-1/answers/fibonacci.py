i = 0
first = 0
second = 1

print("Input number: ", end = "")
number = input()

print(first)

while i < int(number):
    first = first + second
    second = first - second

    print(first)
    i += 1