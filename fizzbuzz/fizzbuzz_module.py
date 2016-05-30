def fizzbuzz(number):
	if number%15 == 0:
		print('FizzBuzz')
	elif number %3 == 0:
		print("Fizz")
	elif number%5 == 0:
		print("Buzz")
	else:
		print(number)
	return number

def main():
	for i in range(1,101):
		fizzbuzz(i)
	return i

if __name__ == '__main__':
    main()
