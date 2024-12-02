with open("input.txt") as inputFile:
    safe = 0
    for textLine in inputFile.readlines():
        line = [int(val) for val in textLine.split()]

        for i in range(-1, len(line)):
            lineVersion = line.copy()
            if i >= 0:
                del lineVersion[i]

            ordered = False
            original_line = lineVersion.copy()
            lineVersion.sort(reverse=True)
            if original_line == lineVersion:
                ordered = True
            lineVersion.sort()
            if original_line == lineVersion:
                ordered = True

            if not ordered:
                continue


            lastVal = lineVersion[0]
            unsafe = False
            for val in lineVersion[1:]:
                if (val - lastVal) not in (1,2,3):
                    unsafe = True
                    break
                lastVal = val

            if not unsafe:
                safe += 1
                break

    print(safe)