


def main():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    total, temp = [], []
    for line in lines:
        if line == "":
            total.append(sum(temp))
            temp = []
        else:
            temp.append(int(line))
    # exercise 1
    print(max(total))
    # exercise 2
    sorted_total = sorted(total)
    print(sum(sorted_total[-3:]))


if __name__ == "__main__":
    main()