def palindrome(pal):
	pal = pal.lower()
	pal = pal.replace(" ", "")
	if pal == pal[::-1]:
		return True
	else:
		print("false")
		return False


def main():
	pal = str(input("Say something: "))
	palindrome(pal)
	return


if __name__ == '__main__':
	main()
