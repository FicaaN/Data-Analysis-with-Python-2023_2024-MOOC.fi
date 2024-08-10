import re


def file_listing(filename="src/listing.txt"):
    pattern = re.compile(
        r"^\S+\s+"  # Access rights
        r"\d+\s+"  # Number of references
        r"\S+\s+"  # Owner's name
        r"\S+\s+"  # Name of owning group
        r"(\d+)\s+"  # File size (group 1)
        r"(\w+)\s+"  # Month (group 2)
        r"(\d+)\s+"  # Day (group 3)
        r"(\d+):(\d+)\s+"  # Hour and minute (group 4 and 5)
        r"(.+)$"  # Filename (group 6)
    )

    result = []

    with open(filename, "r") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                filename = match.group(6)

                result.append((size, month, day, hour, minute, filename))

    return result


def main():
    file_list = file_listing()
    for file_info in file_list:
        print(file_info)


if __name__ == "__main__":
    main()
