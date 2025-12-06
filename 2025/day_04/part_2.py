def read_input(file_path: str) -> list[list[str]]:
	with open(file_path, "r") as f:
		return [list(line) for line in f.read().splitlines()]


def count_adjacent_rolls(grid, r, c) -> int:
	rows, cols = len(grid), len(grid[0])
	directions: list[tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	count: int = 0

	for dr, dc in directions:
		nr, nc = r + dr, c + dc

		if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
			count += 1

	return count


def main() -> None:
	grid: list[list[str]] = read_input("input.txt")
	number_of_removable_rolls: int = 0

	while True:
		number_of_accessible_rolls: int = 0

		for row in range(len(grid)):
			for col in range(len(grid[row])):
				if grid[row][col] == "@" and count_adjacent_rolls(grid, row, col) < 4:
					number_of_accessible_rolls += 1
					grid[row][col] = "."

		if number_of_accessible_rolls > 0:
			number_of_removable_rolls += number_of_accessible_rolls
		else:
			break

	print(f"Number of rolls of paper removable by forklifts: {number_of_removable_rolls}")


if __name__ == "__main__":
	main()
