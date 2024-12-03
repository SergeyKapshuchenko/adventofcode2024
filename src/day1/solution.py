def find_distance(first: list[int], second: list[int]) -> int:
    first = sorted(first)
    second = sorted(second)
    return sum(abs(first[i] - second[i]) for i in range(len(first)))


def read_input(file_path: str) -> tuple[list[int], list[int]]:
    with open(file_path, mode="r") as file:
        data = [line.split() for line in file]
    return [int(first) for first, _ in data], [int(second) for _, second in data]


if __name__ == "__main__":
    first_list, second_list = read_input("input.txt")
    distance = find_distance(first_list, second_list)
    print(distance)