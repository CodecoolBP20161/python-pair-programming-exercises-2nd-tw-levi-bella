import random
# chars = ("!@$%^&*()#?", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789")
# index = random.randint(0, len(chars)-1)
# index2 = random.randint(0, len(chars[index])-1)
# password.append(chars[index][index2])

a=("!@$%^&*()#?")
b=("abcdefghijklmnopqrstuvwxyz")
c=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
d= ("0123456789")
def passwordgen():
	password = []
	while len(password) != 8:
		for i in range(2):
			index = random.randint(0, len(a)-1)
			password.append(a[index])
		for i in range(2):
			index = random.randint(0, len(b)-1)
			password.append(b[index])
		for i in range(2):
			index = random.randint(0, len(c)-1)
			password.append(c[index])
		for i in range(2):
			index = random.randint(0, len(d)-1)
			password.append(d[index])
	random.shuffle(password)
	password = "".join(password)
	return password


def main():
	print(passwordgen())
	return


if __name__ == '__main__':
	main()
