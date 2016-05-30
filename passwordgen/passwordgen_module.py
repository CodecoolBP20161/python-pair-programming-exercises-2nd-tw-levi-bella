import random

def passwordgen():
	chars = ("!@$%^&*()#?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	password = []
	while len(password) != 8:
		index = random.randint(1, len(chars)-1)
		password.append(chars[index])
	password = "".join(password)
	return password


def main():
	passwordgen()
	#print(password)
	return


if __name__ == '__main__':
	main()
