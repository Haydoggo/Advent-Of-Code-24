import re

txt = open("input.txt").read()
running_sum = 0
active = True
for instruction in (re.findall("(mul|do|don't)\((?:(\d+),(\d+))?\)", txt)):
    if instruction[0] == "mul":
        opa, opb = instruction[1:]
        if opa == "" or opb == "":
            continue
        sum += int(opa)*int(opb)
    else:
        active = instruction[0] == "do"
print(running_sum)