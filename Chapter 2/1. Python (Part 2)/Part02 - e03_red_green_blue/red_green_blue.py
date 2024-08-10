import re


def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename, "r") as file:
        next(file)  # This will skip the first line
        for line in file:
            line = line.strip()
            if line:
                match = re.match(r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)", line)
                if match:
                    red, green, blue, colorname = match.groups()
                    formatted_line = f"{red}\t{green}\t{blue}\t{colorname}"
                    result.append(formatted_line)
    return result


def main():
    rgb_list = red_green_blue()
    for color_info in rgb_list:
        print(color_info)


if __name__ == "__main__":
    main()
