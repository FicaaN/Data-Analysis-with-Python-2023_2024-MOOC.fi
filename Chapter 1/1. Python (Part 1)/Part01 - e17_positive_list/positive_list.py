def positive_list(L):
    return list(filter(lambda x: x > 0, L))


def main():
    positive_list([2, -2, 0, 1, -7])


if __name__ == "__main__":
    main()
