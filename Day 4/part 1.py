import re

input_path = "example_input.txt"
input_path = "input.txt"

pattern = ""

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


with open(input_path) as file:
	for text_line in file.readlines():
		grid.append(text_line.removesuffix("\n"))
		h += 1
		w = len(grid[-1])
	print(*grid, sep="\n")

	total_found = 0
	for x_init in range(w):
		for y_init in range(h):
			for direction in ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)):
				found = True
				x = x_init
				y = y_init
				for letter in "XMAS":
					if at(x,y) != letter:
						found = False
						break
					x += direction[0]
					y += direction[1]
				if found:
					total_found += 1
	print(total_found)

