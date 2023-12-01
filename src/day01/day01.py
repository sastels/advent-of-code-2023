import re


day = "01"

numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def read_input(dataType: str):
    with open(f"../../data/day{day}.{dataType}.txt", "r") as f:
        return f.read().splitlines()

    
def just_digits(s: str) -> list:
    return re.sub(r"\D", "", s)


def first_digit(s: str) -> int:
    return int(just_digits(s)[0])


def last_digit(s: str) -> int:
    return int(just_digits(s)[-1])


def part1(data: list):
    return sum(map(lambda s: first_digit(s) * 10 + last_digit(s), data))


## Part 2

def replace_first_number(s: str) -> str:
    to_replace = ("", -1)
    for k in numbers.keys():
        first_k = s.find(k)
        if first_k == -1:
            continue
        elif first_k < to_replace[1] or to_replace[1] == -1:
            to_replace = (k, first_k)
    if to_replace[1] == -1:
        return s
    else:
        return s.replace(to_replace[0], numbers[to_replace[0]], 1)


def replace_last_number(s: str) -> str:
    to_replace = ("", -1)
    for k in numbers.keys():
        last_k = s.rfind(k)
        if last_k == -1:
            continue
        elif last_k > to_replace[1] or to_replace[1] == -1:
            to_replace = (k, last_k)     
    if to_replace[1] == -1:
        return s
    else:
        return numbers[to_replace[0]].join(s.rsplit(to_replace[0], 1))


def first_digit_p2(s: str) -> int:
    return int(just_digits(replace_first_number(s))[0])


def last_digit_p2(s: str) -> int:
    return int(just_digits(replace_last_number(s))[-1])


def part2(data: list):
    return(sum(map(lambda s: first_digit_p2(s) * 10 + last_digit_p2(s), data)))


def main():
    data = read_input("real")
    print(f"Day {day} Part 1: {part1(data)}")
    print(f"Day {day} Part 2: {part2(data)}")


if __name__ == "__main__":
    main()