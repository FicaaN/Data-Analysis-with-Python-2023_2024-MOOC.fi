try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    print(triangle.hypotenuse(10, 12))
    print(triangle.area(10, 12))


if __name__ == "__main__":
    main()
