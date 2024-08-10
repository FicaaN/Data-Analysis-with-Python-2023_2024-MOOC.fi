def sum_equation(L):
    if not L:
        return "0 = 0"

    sum_result = sum(L)
    equation = " + ".join(map(str, L)) + f" = {sum_result}"

    return equation


def main():
    sum_equation([1, 5, 7])


if __name__ == "__main__":
    main()
