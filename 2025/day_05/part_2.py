def read_input(file_path: str) -> list[tuple[int, int]]:
	with open(file_path, "r") as f:
		return [(int(a), int(b)) for a, b in [x.split("-") for x in f.read().split("\n\n")[0].splitlines()]]


def merge_id_ranges(id_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
	if not id_ranges:
		return []

	id_ranges.sort()

	merged_id_ranges: list[tuple[int, int]] = [id_ranges[0]]

	for id_range in id_ranges:
		first_id, last_id = id_range
		prev_first_id, prev_last_id = merged_id_ranges[-1]

		if first_id <= prev_last_id + 1:
			merged_id_ranges[-1] = (prev_first_id, max(prev_last_id, last_id))
		else:
			merged_id_ranges.append(id_range)

	return merged_id_ranges


def main() -> None:
	id_ranges: list[tuple[int, int]] = read_input("input.txt")
	merged_id_ranges: list[tuple[int, int]] = merge_id_ranges(id_ranges)
	number_of_fresh_ids: int = sum(last_id - first_id + 1 for first_id, last_id in merged_id_ranges)

	print(f"Number of fresh ingredient IDs: {number_of_fresh_ids}")


if __name__ == "__main__":
	main()
