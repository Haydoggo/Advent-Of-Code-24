stones : list[int]
with open("input.txt") as file:
	stones = [int(stone) for stone in file.read().split()]

def blink_stone(stone_number)->tuple:
	if stone_number == 0:
		return 1,
	num_digits = len(str(stone_number))
	if (num_digits % 2) == 0:
		num1 = int(str(stone_number)[:num_digits//2])
		num2 = int(str(stone_number)[num_digits//2:])
		return num1, num2
	return (stone_number * 2024,)

for blink in range(25):
	i = 0
	while i < len(stones):
		stone_val = stones[i]
		stones.pop(i)
		for new_val in blink_stone(stone_val):
			stones.insert(i, new_val)
			i += 1
	print(f"{len(stones)} stones after {blink+1} blinks")
print(len(stones))