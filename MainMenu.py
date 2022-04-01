import CaeserCipher
import IOC_Cipher
import Kasiski
import InverseW
import MerkleHellman
import RSA
import DES
import DeffeHellman
import BlockChain
import AESMixcol

def one():
    CaeserCipher.main()
def two():
    IOC_Cipher.main()
def three():
    Kasiski.main()
def four():
    InverseW.main()
def five():
    MerkleHellman.main()
def six():
    RSA.main()
def seven():
    DES.main()
def eight():
    DeffeHellman.main()
def nine():
    BlockChain.main()

def ten():
    print("1. Create Round Key 1")
    print("2. Create state 1")
    print("3. Create State 2")
    print("4. Create state 3")
    print("5. Create state 4(Mutlipy)")
    print("6. Create cipher text")
    choice = input("enter choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        AESMixcol.main()
    elif choice == "6":
        pass
    else:
        print("not valid choice")


def exit():
    print("Ending program...")
    quit()

def choice_switch(arg):
    switcher = {
        0: exit,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10:ten

    }
    func = switcher.get(arg, lambda:"Invalid Choice")
    print (func())

x = ''
while True:
    print("Main Menu")
    print(" 1. Caeser Cipher")
    print(" 2. Incidence of Coincidence")
    print(" 3. Kasiski Key")
    print(" 4. Inverse of W")
    print(" 5. Merkle Hellman(knapsack)")
    print(" 6. RSA")
    print(" 7. DES")
    print(" 8. DeffeHellman")
    print(" 9. Block Chain")
    print(" 10. AES")

    print(" 0. Quit")
    x = input("Enter choice or 0 to quit-> ")
    choice_switch(int(x))

