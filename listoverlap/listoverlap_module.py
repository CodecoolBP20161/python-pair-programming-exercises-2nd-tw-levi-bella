a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def listoverlap(a, b):
	c = sorted(list(set(a).intersection(set(b))))
	print(a, b)
	print(c)
	return c


def main():
	listoverlap(a,b)
	return


if __name__ == '__main__':
    main()
