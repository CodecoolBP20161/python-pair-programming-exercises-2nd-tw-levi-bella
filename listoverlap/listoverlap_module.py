a = [x*2 for x in range(17)]
b = [x for x in range(0, 30, 3)]


def listoverlap(a, b):
    return sorted(list((set(a) & (set(b)))))


def main():
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
