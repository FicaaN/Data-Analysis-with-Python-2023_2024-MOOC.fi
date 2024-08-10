import sys


def file_count(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            number_of_lines = len(lines)
            number_of_words = sum(len(line.split()) for line in lines)
            numer_of_chars = sum(len(line) for line in lines)

            return (number_of_lines, number_of_words, numer_of_chars)

    except FileNotFoundError:
        return (0, 0, 0)


def main():
    for filename in sys.argv[1:]:
        line_count, word_count, char_count = file_count(filename)
        print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")


if __name__ == "__main__":
    main()
