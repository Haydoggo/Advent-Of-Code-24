with open("input.txt") as inputFile:
    safe = 0
    for textLine in inputFile.readlines():
        line = [int(val) for val in textLine.split()]

        ordered = False

        original_line = line.copy()
        line.sort(reverse=True)
        if original_line == line:
            ordered = True
        line.sort()
        if original_line == line:
            ordered = True

        if not ordered:
            continue

        lastVal = line[0]
        unsafe = False
        for val in line[1:]:
            if (val - lastVal) not in (1,2,3):
                unsafe = True
                break
            lastVal = val

        if not unsafe:
            safe += 1

    print(safe)