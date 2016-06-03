import random

spec = ("!@$%^&*()#?")
lows = ("abcdefghijklmnopqrstuvwxyz")
caps = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
nums = ("0123456789")


# 2 characters from all 4 lists
def passwordgen():
    password = []
    while len(password) != 8:
        for i in range(2):
            index = random.randint(0, len(spec)-1)
            password.append(spec[index])
        for i in range(2):
            index = random.randint(0, len(lows)-1)
            password.append(lows[index])
        for i in range(2):
            index = random.randint(0, len(caps)-1)
            password.append(caps[index])
        for i in range(2):
            index = random.randint(0, len(nums)-1)
            password.append(nums[index])
    random.shuffle(password)
    password = ''.join(password)
    return password


# lower- or uppercase letters
def weak():
    password = []
    while len(password) != 8:
        for i in range(4):
            index = random.randint(0, len(caps)-1)
            password.append(caps[index])
        for i in range(4):
            index = random.randint(0, len(lows)-1)
            password.append(lows[index])
    random.shuffle(password)
    password = "".join(password)
    return password


# lower+upper & 2 digits
def medium():
    password = []
    while len(password) != 8:
        for i in range(3):
            index = random.randint(0, len(lows)-1)
            password.append(lows[index])
        for i in range(3):
            index = random.randint(0, len(caps)-1)
            password.append(caps[index])
        for i in range(2):
            index = random.randint(0, len(nums)-1)
            password.append(nums[index])
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
