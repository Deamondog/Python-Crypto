def main():
    while True:
        choice = input("Enter to continue or 'Q'to quit: ")
        if choice == 'Q':
            print("Ending....")
            break
        else:
            g = int(input("Please enter 'g': "))
            p = int(input("Please enter 'p': "))
            x = int(input("Please enter 'x': "))
            y = int(input("Please enter 'y': "))

            half_x=pow(g,x,p)
            half_y=pow(g,y,p)
            key_1=pow(half_x,y,p)
            key_2=pow(half_y,x,p)

            print("Half x: ",half_x,"\nHalf y: ",half_y)
            print("\nKey 1: ",key_1,"\nKey 2: ",key_2)

if __name__ == '__main__':
    main()
