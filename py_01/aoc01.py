with open("input.txt", "r", encoding="utf-8") as file:
    input_lines = [line.strip() for line in file.readlines()]


def parse_digits(line: str) -> str:
    if line.startswith("1"):
        return "1"
    if line.startswith("one"):
        return "1"
    if line.startswith("2"):
        return "2"
    if line.startswith("two"):
        return "2"
    if line.startswith("3"):
        return "3"
    if line.startswith("three"):
        return "3"
    if line.startswith("4"):
        return "4"
    if line.startswith("four"):
        return "4"
    if line.startswith("5"):
        return "5"
    if line.startswith("five"):
        return "5"
    if line.startswith("6"):
        return "6"
    if line.startswith("six"):
        return "6"
    if line.startswith("7"):
        return "7"
    if line.startswith("seven"):
        return "7"
    if line.startswith("8"):
        return "8"
    if line.startswith("eight"):
        return "8"
    if line.startswith("9"):
        return "9"
    if line.startswith("nine"):
        return "9"
    if line.startswith("0"):
        return "0"
    return ""


def task1():
    result = 0
    for line in input_lines:
        if not line:
            continue
        digits = "".join((char for char in line if char.isdigit()))
        result += int(digits[0] + digits[-1])
    return result


def task2():
    result = 0
    for line in input_lines:
        if not line:
            continue
        digits = ""
        for i in range(len(line)):
            digits += parse_digits(line[i:])
        result += int(digits[0] + digits[-1])
    return result


print(task1())
print(task2())
