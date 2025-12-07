def read_input(file_path: str) -> tuple[list[list[int]], list[str]]:
	with open(file_path) as f:
		*number_lines, operator_line = f.read().splitlines()
		number_strs: list[str] = ["".join(number_column).strip() for number_column in zip(*number_lines)]
		number_groups: list[list[int]] = [
			[int(number_str) for number_str in number_group_str.split()]
			for number_group_str in " ".join(number_strs).split("  ")
		]
		operators: list[str] = operator_line.split()

		return number_groups, operators


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
	number_groups, operators = read_input("input.txt")
	operator_function_dict = {"+": add_numbers, "*": multiply_numbers}
	grand_total: int = 0

	for numbers, operator in zip(number_groups, operators):
		grand_total += operator_function_dict[operator](numbers)

	print(f"Grand total: {grand_total}")


if __name__ == "__main__":
	main()
