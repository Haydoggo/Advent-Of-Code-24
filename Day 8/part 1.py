input_path = "input.txt"
# input_path = "example_input.txt"

bound_antinodes_positions = set()

antenna_positions = {} # key = letter, value = list of positions

y = 0
w = h = 0

def get_all_pairs(input_list : list):
	pairs = []
	for i, first in enumerate(input_list):
		for second in input_list[i+1:]:
			pairs.append((first, second))
	return pairs

def get_antinodes(pos1, pos2):
	x1, y1 = pos1
	x2, y2 = pos2
	ax1 = x1 + (x1 - x2)
	ay1 = y1 + (y1 - y2)
	ax2 = x2 + (x2 - x1)
	ay2 = y2 + (y2 - y1)
	return (ax1, ay1), (ax2, ay2)

def in_bounds(x, y):
	global w, h
	return  not (x < 0 or x >= w or y < 0 or y >= h)

with open(input_path) as file:
	for text_line in file.readlines():
		for x, char in enumerate(text_line):
			if char.isalnum():
				if char not in antenna_positions:
					antenna_positions[char] = []
				antenna_positions[char].append((x,y))
		y += 1
		w = len(text_line.removesuffix("\n"))
		h += 1

	for positions in antenna_positions.values():
		for pair in get_all_pairs(positions):
			pos1, pos2 = pair
			a1, a2 = get_antinodes(pos1, pos2)
			if in_bounds(*a1):
				bound_antinodes_positions.add(a1)
			if in_bounds(*a2):
				bound_antinodes_positions.add(a2)

print(len(bound_antinodes_positions))
