import datetime


def years(age):
	year = 2016
	global result
	result = (year - age) + 100
	return result


def main():
	age = 0
	name = input("What's Your name? ")
	age = int(input("How old are you?"))
	years(age)
	print("Hello ",name,"You'll be 100 yrs old in the year of: ", result)
	return age


if __name__ == '__main__':
    main()
