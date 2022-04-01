def meth2(w,n):
    nlinst=[]
    for x in range(1,5000,n):
        nlinst.append(x)
    cnt=0
    for x in range(0,5000,w):
        if x in nlinst:
            return cnt
            break;
        cnt+=1

def main():
    while True:
        text = input("Press enter to continue or 'Q' to quit:")
        if text == "Q":
            print("Ending Inverse W...")
            break
        else:
            try:
                w = int(input("Input value of w: "))
                n = int(input("Input value of n: "))
                print("Method 1 answer: ", pow(w, (n-2),n))
                print("Method 2 answer: ",meth2(w, n))
                print("Method 3 answer: ", pow(w,w,n))
            except:
                print("Enter an number")
                w=0
                n=0

if __name__ == "__main__":
    main()
