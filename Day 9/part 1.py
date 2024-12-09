from turtledemo.penrose import start

input_path = "example_input.txt"
input_path = "input.txt"


def main():
	checksum = 0
	disk_map : str
	with open(input_path) as file:
		disk_map = file.read().strip()
	disk_content = get_content_from_map(disk_map)
	compress_disk(disk_content)
	checksum = get_checksum(disk_content)
	print(checksum)

def get_content_from_map(disk_map) -> list[int]:
	content : list[int] = []
	is_file = True # alternates between true and false as we read files and spaces
	file_id = 0
	for size in [int(entry) for entry in disk_map]:
		content += [file_id if is_file else -1] * size
		if is_file:
			file_id += 1
		is_file = not is_file
	return content

def compress_disk(disk_content):
	start_index = 0
	end_index = len(disk_content)-1

	while True:
		while disk_content[start_index] != -1:
			start_index += 1
		while disk_content[end_index] == -1:
			end_index -= 1
		if end_index <= start_index:
			break
		disk_content[start_index] = disk_content[end_index]
		disk_content[end_index] = -1


def get_checksum(disk_content)-> int:
	checksum = 0
	index = 0
	while disk_content[index] != -1:
		checksum += disk_content[index] * index
		index += 1
	return checksum

if __name__ == "__main__":

	main()