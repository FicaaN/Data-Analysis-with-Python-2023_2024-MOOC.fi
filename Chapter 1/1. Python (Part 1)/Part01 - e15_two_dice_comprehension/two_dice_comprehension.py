def main():
    combinations = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    pairs = [pair for pair in combinations if sum(pair) == 5]

    for pair in pairs:
        print(pair)


if __name__ == "__main__":
    main()
