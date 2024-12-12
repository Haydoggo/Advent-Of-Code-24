from curses.ascii import controlnames


class Grid:
	content: list[str] = []
	w: int = 0
	h: int = 0

	def at(self, pos):
		x, y = pos
		if x < 0 or x >= self.w:
			return "~"
		if y < 0 or y >= self.h:
			return "~"
		return self.content[y][x]

	def populate_from_text(self, text: str):
		for line in text.split("\n"):
			self.h += 1
			self.w = len(line)
			self.content.append(line)


def pos_sum(p1, p2):
	return p1[0] + p2[0], p1[1] + p2[1]


# directions
N, E, W, S = [(0, -1), (1, 0), (-1, 0), (0, 1)]
NE = pos_sum(N, E)
SE = pos_sum(S, E)
SW = pos_sum(S, W)
NW = pos_sum(N, W)


def find_regions(grid: Grid):
	checked_cells = set()
	regions: list[set] = []
	for y in range(grid.h):
		for x in range(grid.w):
			pos = (x, y)
			if pos in checked_cells:
				continue
			cells = set()
			get_region_cells(grid, pos, grid.at(pos), cells)
			checked_cells |= cells
			regions.append(cells)
	return regions


# recursively find all neighbouring cells
def get_region_cells(grid: Grid, pos, crop, cells):
	cells.add(pos)
	x, y = pos
	for dx, dy in N, E, W, S:
		neighbour = (x + dx, y + dy)
		if grid.at(neighbour) == crop and neighbour not in cells:
			get_region_cells(grid, neighbour, crop, cells)


def get_region_price(region: set):
	# The number of walls is equal to the number of corners, so just look for corners
	num_walls = 0
	directions = N, NE, E, SE, S, SW, W, NW
	for cell in region:
		for i in (1,3,5,7): # only look and diagonal cells, as these are where the corners can be
			direction = directions[i]
			if pos_sum(cell, direction) not in region:
				# look for internal corners
				if pos_sum(cell, directions[(i + 1) % 8]) in region and\
				pos_sum(cell, directions[i - 1]) in region:
					num_walls += 1
			# look for external corners
			if pos_sum(cell, directions[(i + 1) % 8]) not in region and \
				pos_sum(cell, directions[i - 1]) not in region:
				num_walls += 1

	area = len(region)
	return num_walls * area


def main():
	input_path = "input.txt"
	# input_path = "example_input.txt"

	grid = Grid()
	with open(input_path) as file:
		grid.populate_from_text(file.read())

	total_price = 0
	regions = find_regions(grid)
	for region in regions:
		total_price += get_region_price(region)

	print(total_price)


main()
