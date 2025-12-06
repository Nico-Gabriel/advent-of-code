def read_input(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
	with open(file_path, "r") as f:
		id_ranges_str, ids_str = f.read().split("\n\n")
		id_ranges: list[tuple[int, int]] = [
			(int(first_id), int(last_id))
			for first_id, last_id in [id_range.split("-") for id_range in id_ranges_str.splitlines()]
		]
		ids: list[int] = [int(id) for id in ids_str.splitlines()]

		return id_ranges, ids


def main() -> None:
	id_ranges, ids = read_input("input.txt")
	number_of_fresh_ids: int = 0

	for id in ids:
		for first_id, last_id in id_ranges:
			if first_id <= id <= last_id:
				number_of_fresh_ids += 1
				break

	print(f"Number of available, fresh ingredient IDs: {number_of_fresh_ids}")


if __name__ == "__main__":
	main()
