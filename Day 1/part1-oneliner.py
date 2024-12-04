print(sum(abs(int(L)-int(R)) for L,R in zip(*[sorted(_list) for _list in zip(*[line.split() for line in open("input.txt").readlines()])])))

