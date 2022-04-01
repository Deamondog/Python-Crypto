from collections import Counter

def count_char(text):

    newText = ''
    sumLetters = [0]*26
    numerator = 0
    totalLetter = 0
    denominator = 0
    ioc = 0

    for x in range(len(text)):
        if text[x].isalpha():
            newText = newText+text[x]

    for x in range(len(newText)):
        sumLetters[(ord(newText[x])-65)] += 1

    for x in range(len(sumLetters)):
        print(chr(x+65),"=",sumLetters[x])
        totalLetter = totalLetter + sumLetters[x]
        y = sumLetters[x] * (sumLetters[x]-1)
        numerator = numerator + y

    denominator = totalLetter * (totalLetter-1)
    ioc = numerator/denominator

    res = Counter(newText)
    res = max(res, key = res.get)

    print(sumLetters)
    print ("The most occuring letter is: " + str(res))
    print("Total Letters:", totalLetter)
    print("Numerator:",numerator)
    print("Denominator:", denominator)
    print("The IOC is:", ioc)


def main():
    while True: #text != 'Q':
        text = input("Please enter text for IOC or 'Q' to quit-> ")
        if text =="Q":
            print("Ending IOC..")
            break
        elif text == "" or len(text) < 2 or text.isdecimal() != False:
            print("Plese enter vaild input")
        elif text !="":
            count_char(text.upper())

if __name__ == "__main__":
    main()
