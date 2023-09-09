
import math

print("Enter Value")
i = float(input("> "))

N1 = 1.0 / (1.0 + math.exp(-(1 * i + 1 + 0)))
N2 = 1.0 / (1.0 + math.exp(-(1 * i + 1 + 1)))
N3 = 1.0 / (1.0 + math.exp(-(1 * i + 1 + 2)))
N4 = 1.0 / (1.0 + math.exp(-(1 * i + 1 + 3)))
N5 = 1.0 / (1.0 + math.exp(-(1 * i + 1 + 4)))
N6 = 1.0 / (1.0 + math.exp(-(1 * i + 1 + 5)))

a1 = ((i - N1) + (i - N4)) / 2
a2 = ((i - N2) + (i - N5)) / 2
a3 = ((i - N3) + (i - N6)) / 2
a4 = (a1 + a2 + a3) / 3

print("Guess 1: ", N1 * i)
print("Guess 2: ", N2 * i)
print("Guess 3: ", N3 * i)
print("Guess 4: ", N4 * i)
print("Guess 5: ", N5 * i)
print("Guess 6: ", N6 * i)
print("Neuron Errors")
print("(N1-N4): ", a1 ,"\n(N2-N5): ", a2 , "\n(N3-N6): ", a3)
print("(All N's): ", a4)
