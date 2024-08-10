def detect_ranges(L):
    sorted_list = sorted(L)
    result = []
    start = sorted_list[0]
    current = start

    for number in sorted_list[1:]:
        if number == current + 1:
            current = number
        else:
            if start == current:
                result.append(start)
            else:
                result.append((start, current + 1))

            start = number
            current = start

    if start == current:
        result.append(start)
    else:
        result.append((start, current + 1))

    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
