input_path = "input.txt"
# input_path = "example_input.txt.txt"

calibration_result = 0

with open(input_path) as file:
	for text_line in file.readlines():
		test_val = int(text_line.split(":")[0])
		operands = [int(val) for val in text_line.split(":")[1].split()]

		num_operators = len(operands)-1
		# go over every binary combination
		# 0 = plus, 1 = mult
		for permutation in range(2<<(num_operators-1)):
			operators = []
			for i in range(num_operators):
				bitmask = 1 << i
				if (permutation & bitmask) == 0:
					operators.append("x")
				else:
					operators.append("+")

			# do calculation
			running_value = operands[0]
			for i, operator in enumerate(operators):
				next_operand = operands[i+1]
				if operator == "x":
					running_value *= next_operand
				if operator == "+":
					running_value += next_operand

			if running_value == test_val:
				calibration_result += test_val
				break
	print(calibration_result)


