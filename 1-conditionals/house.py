name = input("ur name?: ")

def match_func():
    match name:
        case "Harry" | "Hermione" |"Ron":
            print("Grify")
        case "Draco":
            print("Slyther")
        case _:
            print("fuck who")

def if_func():
    if(name == "harry" or name == "hermone" or name == "ron"):
        print("grify")
    elif(name=="draco"):
        print("slyther")
    else:
        print("fck who?")
