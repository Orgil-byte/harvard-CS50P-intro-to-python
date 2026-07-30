def printUserName(to="world"):
    print(f"hello {to.title().strip()}!")

printUserName()

name = input("What is ur name?: ")

printUserName(name)
