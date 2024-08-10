def merge(L1, L2):
    i, j = 0, 0
    merged_list = []

    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1

    while i < len(L1):
        merged_list.append(L1[i])
        i += 1

    while j < len(L2):
        merged_list.append(L2[j])
        j += 1

    return merged_list


def main():
    L1 = [1, 2, 3, 4, 5]
    L2 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(merge(L1, L2))


if __name__ == "__main__":
    main()
