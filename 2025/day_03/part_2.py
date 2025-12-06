def read_input(file_path: str) -> list[list[int]]:
	with open(file_path, "r") as f:
		return [[int(num) for num in line] for line in f.read().splitlines()]


def main() -> None:
	banks: list[list[int]] = read_input("input.txt")
	max_joltage_sum: int = 0

	for batteries in banks:
		digits: list[int] = []

		for i in range(11, -1, -1):
			start_index: int = batteries.index(digits[-1]) + 1 if digits else 0
			end_index: int = -i if i != 0 else len(batteries)
			digits.append(max(batteries[start_index:end_index]))
			batteries = batteries[start_index:]

		max_joltage_sum += int("".join(map(str, digits)))

	print(f"Total output joltage: {max_joltage_sum}")


if __name__ == "__main__":
	main()
