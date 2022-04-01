def mixColumns(a, b, c, d):
    printHex(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    printHex(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    print()


def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a


def printHex(val):
    return print('{:02x}'.format(val), end=' ')
    
def main():
    row=[]
    for x in range(16):
        input_string = int(input("Enter HEX number start with row 1: "),16)
        row.append(input_string)
        
    # for x in range(4):
    #         print(hex(row[x]).upper())

    # print(row[0])

    print("row 1: ")
    mixColumns(row[0], row[1], row[2], row[3])  #row 1
    print("row 2: ")
    mixColumns(row[4], row[5], row[6], row[7])  # row 2
    print("row 3: ")
    mixColumns(row[8], row[9], row[10], row[11])  # row 3
    print("row 4: ")
    mixColumns(row[12], row[13], row[14], row[15])  # row 4


if __name__ == "__main__":
    main()






