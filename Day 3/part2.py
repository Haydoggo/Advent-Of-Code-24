with open("input.txt") as inputFile:
    i = 0
    text :str = inputFile.read()
    sum = 0
    active = True
    while i < len(text):
        imult = text.find("mul(", i)
        instruct = text.find("do", i)
        if imult == -1 and instruct == -1:
            break
        doMult = True
        if instruct < imult and instruct != -1:
            doMult = False
        if doMult:
            if not active:
                i += 1
                continue
            if imult == -1:
                i += 1
                continue

            i = imult
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
        else:
            if instruct == -1:
                i+= 1
                continue

            i = instruct
            if text[i:i+4] == "do()":
                active = True
                i+=4
            elif text[i:i+7] == "don't()":
                active = False
                i+=7
            else:
                i+=1
    print(sum)

