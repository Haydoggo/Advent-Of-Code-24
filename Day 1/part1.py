with open("input.txt") as file:
    left :list[int] = list()
    right :list[int] = list()
    for line in file.readlines():
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    s = 0
    for i in range(len(left)):
        s += abs(left[i] - right[i])
    print(s)

