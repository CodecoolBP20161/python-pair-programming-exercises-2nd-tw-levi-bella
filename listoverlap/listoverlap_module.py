a = [x*2 for x in range(17)]
b = [x for x in range(0, 30, 3)]


def listoverlap(a, b):
    c = sorted(list((set(a) & (set(b)))))
    return c


def main():
    print(listoverlap(a, b))
    return


if __name__ == '__main__':
    main()
