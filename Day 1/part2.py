with open("input.txt") as file:
    left :list[int] = list()
    right :list[int] = list()
    rCounts = {}

    for line in file.readlines():
        l,r = line.split()
        l = int(l)
        r = int(r)
        left.append(l)
        right.append(r)
        if r not in rCounts:
            rCounts[r] = 0
        if l not in rCounts:
            rCounts[l] = 0
        rCounts[r] += 1

    left.sort()
    right.sort()
    p = 0
    for i in range(len(left)):
        p += left[i] * rCounts[left[i]]
    print(p)

