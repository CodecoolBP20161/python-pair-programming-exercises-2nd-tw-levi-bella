import datetime


def years(age):
	name = input("What's Your name? ")
	age = int(input("How old are you?"))
	year = 2016
	result = (year - age) + 100
	print("Hello ",name,"You'll be 100 yrs old in the year of: ", result)
	return result


def main():
	age = 0
	years(age)
	return age


if __name__ == '__main__':
    main()
