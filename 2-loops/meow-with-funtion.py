def main():
    num = get_number()
    meow(num)


def get_number():
    while True:
        num = int(input("what is the number? "))
        if(num > 0):
            return num


def meow(num):
    for _ in range(num):
        print("meow")

main()