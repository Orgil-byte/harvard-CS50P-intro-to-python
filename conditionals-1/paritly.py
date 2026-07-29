def main():
    num= int(input("Number: "))
    if(is_even(num)):
        print("even")
    else:
        print("odd")
    

def is_even(num):
    
    return  num % 2 == 0

main()