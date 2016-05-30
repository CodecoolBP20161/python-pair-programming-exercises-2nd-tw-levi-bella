import random

def passwordgen():
	return


def main():
	chars = ("!@$%^&*()#?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	password = []
	while len(password) != 8:
		index = random.randint(1, len(chars)+1)
		password.append(chars[index])
	password = "".join(password)
	print(password)
	passwordgen()
	return


if __name__ == '__main__':
	main()
