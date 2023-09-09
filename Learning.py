import math

i = input("Enter value: ")

if len(i) == 1:
    if i.isalpha():
        ascii_i = ord(i)
        print(f"{i} ASCII value: {ascii_i}")
        number = ascii_i
        w = 1
        b = 1
        for j in range(11):
            w = w + j
            b = b + 1
            sigmoid = 1.0 / (1.0 + math.exp(-(w * number + b)))
            print("Guess:", sigmoid * number)
            if(sigmoid == number):
                print("Guess = ", number)
    elif i.isdigit():
        num = int(i)
        print(f"Inputted number: {num}")
        w = 1
        b = 1
        for j in range(11):
            w = w + j
            b = b + 1
            sigmoid = 1.0 / (1.0 + math.exp(-(w * num + b)))
            print("Guess:", sigmoid * num)
            if(sigmoid == num):
                print("Guess = ", num)
else:
    print("Something went wrong...")

