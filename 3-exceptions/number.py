def main():
    print(get_int())

def get_int():
    while True:
        try:
            x=(int(input("x: ")))
        except ValueError:
            print("x is not a integer")
        else:
            return x

main()