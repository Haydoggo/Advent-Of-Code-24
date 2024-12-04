with open("input.txt") as inputFile:
    i = 0
    text :str = inputFile.read()
    sum = 0
    active = True
    while i < len(text):
        i = text.find("mul(", i)
        if i == -1:
            break
        i += 4
        num1 = 0
        numFound = False
        while text[i].isnumeric():
            num1*=10
            num1 += int(text[i])
            numFound = True
            i += 1
        if not numFound:
            continue
        if text[i] != ",":
            continue
        i += 1
        num2 = 0
        numFound = False
        while text[i].isnumeric():
            num2 *= 10
            num2 += int(text[i])
            numFound = True
            i += 1
        if not numFound:
            continue
        if text[i] != ")":
            continue
        i+=1
        sum += num1 * num2
    print(sum)

