def file_extensions(filename):
    no_extensions = []
    extensions = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if "." in line:
                parts = line.rsplit(".", 1)
                if len(parts) == 2:
                    name, ext = parts
                    if ext in extensions:
                        extensions[ext].append(line)
                    else:
                        extensions[ext] = [line]
            else:
                no_extensions.append(line)

    return (no_extensions, extensions)


def main():
    filename = "src/filenames.txt"
    no_extensions, extensions = file_extensions(filename)

    print(f"{len(no_extensions)} files with no extension")

    for extension in sorted(extensions):
        print(f"{extension} {len(extensions[extension])}")


if __name__ == "__main__":
    main()
