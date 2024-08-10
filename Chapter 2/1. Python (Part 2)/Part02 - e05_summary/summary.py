import sys
import math


def summary(filename):
    list_of_numbers = []

    with open(filename, "r") as file:
        for line in file:
            try:
                number = float(line.strip())
                list_of_numbers.append(number)
            except ValueError:
                continue

    n = len(list_of_numbers)
    if n == 0:
        return (0.0, 0.0, 0.0)

    sum_numbers = sum(list_of_numbers)
    average = sum_numbers / n
    stddev = math.sqrt(sum((x - average) ** 2 for x in list_of_numbers) / (n - 1) if n > 1 else 0.0)

    return (sum_numbers, average, stddev)


def main():
    for filename in sys.argv[1:]:
        sum_numbers, average, stddev = summary(filename)
        print(
            f"File: {filename} Sum: {sum_numbers:.6f} Average: {average:.6f} Stddev: {stddev:.6f}"
        )


if __name__ == "__main__":
    main()
