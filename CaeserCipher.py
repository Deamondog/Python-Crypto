from collections import Counter
from string import whitespace

def runTxt(text, shift):
    newText = ''
    for x in range(len(text)):
        if text[x].isalpha():
            newText += chr((ord(text[x]) + shift-65) % 26 + 65)
        else:
            newText = newText[:x] + " " + newText[x:]
    return newText

def decrypt(text):
    while True:
        ans = input("Is shift known? 'Y/N': ")
        if ans == "Y":
            shift = int(input("enter shift: "))
            shift = 26-shift
            decryptText = runTxt(text,shift)
            print("Encoded Text: ",text, end='\n')
            print("Decoded Text: ", decryptText, end='\n')
            break

        elif ans == "N":
            for x in range(26):
                decryptText = runTxt(text,x)
                print(x,":", decryptText, end='\n')
            break

        elif ans != "N" or ans != "Y":
            print("Enter Valid answer")

def encrypt(text,shift):
    encryptText = runTxt(text,shift)
    print("Decoded Text: ",text, end='\n')
    print("Encoded Text: ",encryptText, end='\n')

#-----------Main------------
def main():
    while True:
        #enter choice
        choice = input("Enter 1 to encode or 2 to decode or 'Q' to quit-> ")
        #ends program if Q entered
        if choice == "Q":
            print("Ending Ceaser Cipher...")
            break
        #runs the ceaser encryption
        elif choice == "1":
            txt = input("Enter text to encode-> ")
            shift = input("enter shift: ")
            encrypt(txt.upper(),int(shift))
        #runs the ceaser decryption
        elif choice == "2":
            txt = input("Enter text to decode-> ")
            decrypt(txt.upper())
        else:
            print("Please enter valid choice.")

if __name__ == "__main__":
    main()
