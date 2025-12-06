def read_input(file_path: str) -> list[tuple[int, int]]:
	with open(file_path, "r") as f:
		return [(int(a), int(b)) for a, b in [x.split("-") for x in f.read().split(",")]]


def main() -> None:
	id_ranges: list[tuple[int, int]] = read_input("input.txt")
	invalid_id_sum: int = 0

	for first_id, last_id in id_ranges:
		for current_id in range(first_id, last_id + 1):
			current_id_str: str = str(current_id)

			if current_id_str in (current_id_str * 2)[1:-1]:
				invalid_id_sum += current_id

	print(f"Invalid ID sum: {invalid_id_sum}")


if __name__ == "__main__":
	main()
