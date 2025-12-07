def read_input(file_path: str) -> tuple[list[list[int]], list[str]]:
	with open(file_path, "r") as f:
		lines: list[list[str]] = [line.split() for line in f.read().splitlines()]
		number_lines: list[list[int]] = [list(map(int, line)) for line in lines[:-1]]
		operator_line: list[str] = lines[-1]

		return number_lines, operator_line


def add_numbers(numbers: list[int]) -> int:
	return sum(numbers)


def multiply_numbers(numbers: list[int]) -> int:
	if not numbers:
		return 0

	product: int = 1

	for number in numbers:
		product *= number

	return product


def main() -> None:
	number_lines, operator_line = read_input("input.txt")
	operator_function_dict = {"+": add_numbers, "*": multiply_numbers}
	grand_total: int = 0

	for numbers, operator in zip(map(list[int], zip(*number_lines)), operator_line):
		grand_total += operator_function_dict[operator](numbers)

	print(f"Grand total: {grand_total}")


if __name__ == "__main__":
	main()
