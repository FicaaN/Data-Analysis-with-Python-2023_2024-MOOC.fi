def main():
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)

    for row in table:
        print(" ".join(f"{number:3}" for number in row))


if __name__ == "__main__":
    main()
