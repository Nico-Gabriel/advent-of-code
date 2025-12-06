def read_input(file_path: str) -> list[str]:
	with open(file_path, "r") as f:
		return f.read().splitlines()


def main() -> None:
	rotations: list[str] = read_input("input.txt")
	dial: int = 50
	zeroCounter: int = 0

	for rotation in rotations:
		direction, distance = rotation[0], int(rotation[1:])

		if direction == "L":
			for _ in range(distance):
				dial -= 1
				if dial < 0:
					dial = 99
				if dial == 0:
					zeroCounter += 1
		elif direction == "R":
			for _ in range(distance):
				dial += 1
				if dial > 99:
					dial = 0
				if dial == 0:
					zeroCounter += 1

	print(f"Password: {zeroCounter}")


if __name__ == "__main__":
	main()
