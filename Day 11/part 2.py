stones : dict[int, int] = {}

def add_stone(stone_val, times):
	if stone_val not in stones:
		stones[stone_val] = 0
	stones[stone_val] += times

with open("input.txt") as file:
	for stone_val in [int(stone) for stone in file.read().split()]:
		add_stone(stone_val, 1)

def blink_stone(stone_number)->tuple:
	if stone_number == 0:
		return 1,
	num_digits = len(str(stone_number))
	if (num_digits % 2) == 0:
		num1 = int(str(stone_number)[:num_digits//2])
		num2 = int(str(stone_number)[num_digits//2:])
		return num1, num2
	return (stone_number * 2024,)

for blink in range(75):
	old_stones = stones.copy()

	for stone_val in old_stones:
		stone_multiplier = old_stones[stone_val]
		add_stone(stone_val, -stone_multiplier)
		for new_val in blink_stone(stone_val):
			add_stone(new_val, stone_multiplier)
	print(f"{sum(stones.values())} stones after {blink+1} blinks")
	# print(sorted(stones.keys()))
total_stones = sum(stones.values())
