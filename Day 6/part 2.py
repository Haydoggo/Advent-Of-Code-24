from time import time

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

	print(f"w = {w}, h = {h}, spots to search = {w*h}")


	start_x = x
	start_y = y

	num_valid_locations = 0
	spots_searched = 0
	start_time = time()
	for obx in range(w):
		for oby in range(h):
			spots_searched += 1
			if spots_searched % 100 == 0:
				print(f"searched {spots_searched} out of {w*h}")
			if at(obx,oby) != ".":
				continue
			grid[oby][obx] = "#"

			location_history = set()
			x = start_x
			y = start_y
			direction = directions[0]

			while at(x, y) != "~":
				location = (x, y, direction)
				if location in location_history:
					num_valid_locations += 1
					break
				location_history.add(location)

				next_cell = at(x + direction[0], y + direction[1])

				if next_cell == "#":  # turn on wall
					direction = directions[(directions.index(direction) + 1) % len(directions)]
				else:  # move
					x += direction[0]
					y += direction[1]

			grid[oby][obx] = "."
	end_time = time()
	print(f"finished in {end_time - start_time:.2f} seconds")