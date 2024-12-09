from enum import unique

input_path = "input.txt"
# input_path = "example_input.txt.txt"

grid = []
w = 0
h = 0

def at(x,y):
	global grid, w, h
	if x < 0 or x >= w:
		return "~"
	if y < 0 or y >= h:
		return "~"
	return grid[y][x]

directions = [(0,-1), (1,0), (0,1), (-1,0)]
direction = directions[0]

with open(input_path) as file:
	x = y = 0
	for text_line in file.readlines():
		grid.append(list(text_line.removesuffix("\n")))
		h += 1
		w = len(grid[-1])
		if "^" in text_line:
			x = text_line.index("^")
			y = h-1


	unique_spots = 0
	while at(x,y) != "~":
		next_cell = at(x + direction[0], y + direction[1])
		print(*grid, sep="\n")
		print("-----")

		if next_cell == "#": # turn on wall
			direction = directions[(directions.index(direction) + 1) % len(directions)]
		else: # move
			if at(x,y) != "X":
				unique_spots += 1
			grid[y][x] = "X"

			x += direction[0]
			y += direction[1]

	print(unique_spots)
	print(*grid, sep="\n")
