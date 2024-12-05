import re


input_path = "example_input.txt"
input_path = "input.txt"

numbers_ahead = {} # key: number, value: set of numbers that must be afterward
numbers_behind = {}# key: number, value: set of numbers that must be before

middle_sum = 0

def check_row():
	for i in range(len(row)):
		found_nums_ahead = set(row[i + 1:])
		found_nums_behind = set(row[:i])
		num = row[i]
		if numbers_ahead.get(num, set()) & found_nums_behind \
		or numbers_behind.get(num, set()) & found_nums_ahead:
			return False
	return True

with open(input_path) as file:
	text_line = file.readline()
	while "|" in text_line:
		num1, num2 = text_line.strip().split("|")
		if num1 not in numbers_ahead:
			numbers_ahead[num1] = set()
		if num2 not in numbers_behind:
			numbers_behind[num2] = set()
		numbers_ahead[num1].add(num2)
		numbers_behind[num2].add(num1)

		text_line = file.readline()

	text_line = file.readline() # skip blank line

	while len(text_line) > 0:
		row = text_line.strip().split(",")
		text_line = file.readline()
		if check_row():
			middle_val = int(row[len(row)//2])
			print(middle_val)
			middle_sum += middle_val


print(middle_sum)

