input_path = "input.txt"
# input_path = "example_input.txt.txt"

calibration_result = 0

with open(input_path) as file:
	line_num = 0
	for text_line in file.readlines():
		print(line_num)
		line_num+= 1
		test_val = int(text_line.split(":")[0])
		operands = [int(val) for val in text_line.split(":")[1].split()]

		num_operators = len(operands)-1
		# go over every trinary combination
		# 0 = plus, 1 = mult, 2 = concat
		for permutation in range(3**num_operators):
			operators = []
			for i in range(num_operators):
				operator = permutation % 3
				operators.append(("+", "x", "||")[operator])
				permutation //= 3

			# do calculation
			running_value = operands[0]
			for i, operator in enumerate(operators):
				next_operand = operands[i+1]
				if operator == "x":
					running_value *= next_operand
				if operator == "+":
					running_value += next_operand
				if operator == "||":
					running_value = int(str(running_value) + str(next_operand))

			if running_value == test_val:
				calibration_result += test_val
				break
	print(calibration_result)