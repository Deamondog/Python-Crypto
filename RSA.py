def get_pqe():
    p = int(input("Please enter 'p': "))
    q = int(input("Please enter 'q': "))
    e = int(input("Please enter 'e': "))
    return p,q,e

def compare():
    input_res = get_pqe()
    totN = (input_res[0]-1)*(input_res[1]-1)
    # print(totN)

    nlinst=[]
    for x in range(1,5000,totN):
        nlinst.append(x)
    cnt=0
    for x in range(0,5000,input_res[2]):
        if x in nlinst:
            print(cnt)
            return cnt
            break;
        cnt+=1

def calc_c():
    input_res = get_pqe()
    d = int(input("Please enter 'd': "))
    P = int(input("Please enter 'P': "))
    print(end='\n')
    n = input_res[0] * input_res[1]
    c_result = pow(P,input_res[2],n)
    print("'C' is: ",c_result, end='\n'*2)

def calc_p():
    input_res = get_pqe()
    d = int(input("Please enter 'd': "))
    C = int(input("Please enter 'C': "))
    print(end='\n')
    n = input_res[0] * input_res[1]
    p_result = pow(C,d,n)
    print("'P' is: ",p_result, end='\n'*2)


#------Main------------

def main():
    while True:
        print("RSA Main Menu\n", "1. Find d\n", "2. Calculate P\n", "3. Calculate C\n","0. Exit\n")
        choice = input("Please enter Choice:  ")

        if choice == "0":
            print("Ending...")
            break
        elif choice == "1":
            print("Finding 'd'.\n")
            print("'d' is: ", compare(),end='\n'*2)
        elif choice =="2":
            print("Calculating P\n")
            calc_p()
        elif choice == "3":
            print("Calculating C\n")
            calc_c()
        else:
            print("Enter valid choice.",end='\n'*2)



if __name__ == "__main__":
    main()
