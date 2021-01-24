numGreater90 = []
score = 0
while score >= 0:
    score = int(input("Put a number, to exit enter a negative number: "))
    if score >= 90:
        userInputs.append(score)
        numGreater90.append(score)
    elif score >= 0:
        userInputs.append(score)
    else:
        print("number is out of range")
print(userInputs)
print(numGreater90)
print("Bigger than 90: ", len(numGreater90))
print("Avarege: ", sum(userInputs)/len(userInputs))
