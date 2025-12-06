def read_input(file_path: str) -> list[list[int]]:
	with open(file_path, "r") as f:
		return [[int(num) for num in line] for line in f.read().splitlines()]


def main() -> None:
	banks: list[list[int]] = read_input("input.txt")
	max_joltage_sum: int = 0

	for batteries in banks:
		a: int = max(batteries[:-1])
		b: int = max(batteries[batteries.index(a) + 1 :])
		max_joltage_sum += a * 10 + b

	print(f"Total output joltage: {max_joltage_sum}")


if __name__ == "__main__":
	main()
