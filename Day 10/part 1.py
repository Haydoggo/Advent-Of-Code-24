class Grid:
	content : list[list[int]] = []
	w : int = 0
	h : int = 0

	def at(self, x, y):
		if x < 0 or x >= self.w:
			return "~"
		if y < 0 or y >= self.h:
			return "~"
		return self.content[y][x]

	def populate_from_text(self, text:str):
		for line in text.split("\n"):
			self.h += 1
			self.w = len(line)
			self.content.append([int(c) if c.isnumeric() else c for c in line])

directions = [(0,-1), (1,0), (0,1), (-1,0)]
direction = directions[0]

def get_trail_score(grid, x, y):
	found = set()
	recursive_search(grid, x, y, 1, found)
	return len(found)

def recursive_search(grid, x, y, next_target, found : set):
	for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
		nx = x + dx
		ny = y + dy
		n = grid.at(nx, ny)
		if n == next_target:
			if next_target == 9:
				found.add((nx,ny))
			else:
				recursive_search(grid, nx, ny, next_target + 1, found)

def main():
	input_path = "input.txt"
	# input_path = "example_input.txt"

	sum_score = 0
	grid = Grid()
	with open(input_path) as file:
		grid.populate_from_text(file.read())

	for x in range(grid.w):
		for y in range(grid.h):
			if grid.at(x,y) == 0:
				score = get_trail_score(grid, x, y)
				print(score)
				sum_score += score
	print(sum_score)



main()