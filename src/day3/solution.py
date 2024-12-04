import re


def multiply(string: str, enabled: bool = False) -> int:
    result = 0
    mul_enabled = True
    if enabled:
        pattern = r"mul\(\d+,\s*\d+\)|do\(\)|don't\(\)"
    else:
        pattern = r"mul\(\d+,\s*\d+\)"

    for item in re.findall(pattern, string):
        match item:
            case "don't()":
                mul_enabled = False
            case "do()":
                mul_enabled = True
            case _:
                if mul_enabled:
                    x, y = (int(i) for i in re.findall(r"\d+", item))
                    result += x * y

    return result


def read_input(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


if __name__ == "__main__":
    string = read_input("input.txt")

    # part 1
    print(multiply(string))

    # part 2
    print(multiply(string, True))
