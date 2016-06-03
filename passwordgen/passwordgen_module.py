import random

a = ("!@$%^&*()#?")
b = ("abcdefghijklmnopqrstuvwxyz")
c = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
d = ("0123456789")


a = ("!@$%^&*()#?")
b = ("abcdefghijklmnopqrstuvwxyz")
c = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
d = ("0123456789")


# 2 characters from all 4 lists
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
    password = ''.join(password)
    return password


# lower- or uppercase letters
def weak():
    password = []
    while len(password) != 8:
        for i in range(4):
            index = random.randint(0, len(c)-1)
            password.append(c[index])
        for i in range(4):
            index = random.randint(0, len(b)-1)
            password.append(b[index])
    random.shuffle(password)
    password = "".join(password)
    return password


# lower+upper & 2 digits
def medium():
    password = []
    while len(password) != 8:
        for i in range(3):
            index = random.randint(0, len(b)-1)
            password.append(b[index])
        for i in range(3):
            index = random.randint(0, len(c)-1)
            password.append(c[index])
        for i in range(2):
            index = random.randint(0, len(d)-1)
            password.append(d[index])
    random.shuffle(password)
    password = "".join(password)
    return password


def main():
    diff = input("Choose password security! => hard/med/weak: ")
    if diff == "hard":
        print(passwordgen())
    if diff == "med":
        print(medium())
    if diff == "weak":
        print(weak())
    return


if __name__ == '__main__':
    main()
