import itertools
import InverseW

#def to convert list to intergers
def convert2int(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return

#calculates the hard knapsack
def hardknapsack(w,n,s):
    h = []
    for x in range(len(s)):
        x = w * s[x] % n
        h.append(x)
    return h

def decrypt(w, n, simple):
    input_string = input("Enter cipher use 'space' for seperation: ")
    cipher=input_string.split()
    convert2int(cipher)
    newCipher = []

    for x in range(len(cipher)):
        x = w * cipher[x] % n
        newCipher.append(x)
    for ms in range(len(newCipher)):
        decrypt=newCipher[ms]
        for i in range(1,len(simple)+1):
            for j in itertools.combinations(simple, i):
                tempsum=0
                for x in range(len(j)):
                    tempsum+=j[x]
                if tempsum == decrypt:
                    for y in range(len(simple)):
                        if simple[y] in j:
                            print(1, end="")
                        else:
                            print(0, end="")
                    print(" ", end="")

    print("\n")

def encrypt(hardk):

    input_string2 = input("Enter plaintxt use 'space' for speration: ")
    plain = input_string2.split()
    convert2int(plain)

    r = hardk * int(len(plain)/len(hardk))
    products = [r[i]*plain[i] for i in range(len(plain))]

    final = [products[i * (len(hardk)):(i + 1) * (len(hardk))] for i in range((len(products) + (len(hardk)) - 1) // (len(hardk)) )]

    c=[]
    for x in range(len(final)):
        c.append(sum(final[x]))
    print("Chiper text is: ",c)


def getInput(z):
    w = int(input("W: "))
    n = int(input("N: "))

    input_string = input("Enter "+z+" elements use 'space' for speration: ")
    s=input_string.split()
    convert2int(s)

    return w,n,s



def main():
    while True:
        print("Main Menu\n 1. Calculate hardknapsack\n 2. Encrypt\n 3. Decrypt with Cipher\n 4. Calculate Inverse W\n 0. Quit")
        choice = input("Please enter Choice: ")

        if choice == "0":
            print("Ending...")
            break
        elif choice == "1":
            print("Calculation Hard knapsack\n")
            w = getInput("Simple Knapsack")
            print(hardknapsack(w[0],w[1],w[2]))
        elif choice =="2":
            print("Calculate encryption\n")
            w = getInput("Simple Knapsack")
            encrypt(hardknapsack(w[0],w[1],w[2]))
        elif choice == "3":
            print("Calculate cipher decryption\n","W is w^-1")
            w = getInput("Simple Knapsack")
            decrypt(w[0],w[1],w[2])
        elif choice == "4":
            InverseW.main()

if __name__ == "__main__":
    main()
