import math
print("Enter Weight")
w = float(input("> "))
print("Enter Bias")
b = float(input("> "))
print("Enter a value")
i = float(input("> "))
sigma = 1
ni = w * i + b
sigmoid = 1.0 / (1.0 + math.exp(-ni))
print("Guess: ", sigmoid * i)

