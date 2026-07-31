def main():
    print_column(3)
    print_row(4)
    print_square(3)
    print_square_simpler(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(length):

    #for _ in each row in square 
    for _ in range(length):

        #for j  in each # in row 
        for j in range(length):

            #print("#") print each one #
            print("# ", end=" ")

        #print() will make for j in start from new line    
        print()

def print_square_simpler(length):

    for _ in range(length):
        print("@  "  * length)


main()