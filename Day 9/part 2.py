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

class Block:
	file_id: int
	size: int

	def __repr__(self):
		if self.file_id == -1:
			return "."*self.size
		else:
			return str(self.file_id) * self.size

	def copy(self):
		new_block = Block()
		new_block.file_id = self.file_id
		new_block.size = self.size
		return new_block

	def __str__(self):
		return self.__repr__()

def get_content_from_map(disk_map) -> list[Block]:
	content : list[Block] = []
	is_file = True # alternates between true and false as we read files and spaces
	file_id = 0
	for size in [int(entry) for entry in disk_map]:
		if size >= 1:
			block = Block()
			block.file_id = file_id if is_file else -1
			block.size = size
			content.append(block)
		if is_file:
			file_id += 1
		is_file = not is_file
	return content

def compress_disk(disk_content):
	start_index = 0

	for file in [block for block in reversed(disk_content) if block.file_id >= 0]:
		file_index = disk_content.index(file)

		# find the first gap that fits:
		for i, block in enumerate(disk_content):
			if i >= file_index:
				break
			if block.file_id == -1 and block.size >= file.size:
				# if it fits perfectly, replace the gap
				if file.size == block.size:
					disk_content[i] = file.copy()

				# otherwise cut into the free block
				else:
					block.size -= file.size
					disk_content.insert(i, file.copy())
					file_index += 1
				file.file_id = -1
				break


def get_checksum(disk_content)-> int:
	checksum = 0
	index = 0
	for block in disk_content:
		if block.file_id == -1:
			index += block.size
		else:
			for j in range(block.size):
				checksum += index * block.file_id
				index += 1
	return checksum

if __name__ == "__main__":

	main()