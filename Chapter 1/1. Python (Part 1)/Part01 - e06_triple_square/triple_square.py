def triple(x):
    return x * 3


def square(x):
    return x**2


def main():
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if s > t:
            break
        print(f"triple({i})=={t} square({i})=={s}")


if __name__ == "__main__":
    main()
