class Prepend(object):
    def __init__(self, string: str):
        self.string = string

    def write(self, string1: str):
        print(f"{self.string}{string1}")


def main():
    p = Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()
