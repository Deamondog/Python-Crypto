hex_res=[]
bin_res=[]

def convertHex(input_str):
    for ch in input_str:
        hex_res.append(hex(ord(ch)).lstrip('0x').upper().zfill(2))
    return hex_res


def convertBin(input_str):
        for ch in input_str:
            bin_res.append(bin(ord(ch)).lstrip('0b').upper().zfill(8))
        return bin_res

def convertBinHex(array_in):
    temp=''
    out_array = []
    x = 0
    rangeEnd = len(array_in)/8
    for y in range(0,int(rangeEnd)):
        temp = ''
        for x in range (x, x+8):
            temp = temp+array_in[x]
            x=x+1
        out_array.append(hex(int(temp,2)).replace('0x','').upper().zfill(2))
    return out_array

def ip(bin_array):

    initialSchema = [58,50,42,34,26,18,10,2,
                     60,52,44,36,28,20,12,4,
                     62,54,46,38,30,22,14,6,
                     64,56,48,40,32,24,16,8,
                     57,49,41,33,25,17,9,1,
                     59,51,43,35,27,19,11,3,
                     61,53,45,37,29,21,13,5,
                     63,55,47,39,31,23,15,7]

    bin_out = list(range(64))
    for x in range(0, len(bin_array)):
        bin_out[x] = bin_array[initialSchema[x]-1]

    tempStr = ''
    for x in range(0,len(bin_out)):
        tempStr = tempStr + bin_out[x]
    return tempStr

def expansionPerm(bin_array_exp):
    expansionSchema = [32,1,2,3,4,5,4,5,
                        6,7,8,9,8,9,10,11,
                        12,13,12,13,14,15,16,17,
                        16,17,18,19,20,21,20,21,
                        22,23,24,25,24,25,26,27,
                        28,29,28,29,30,31,32,1]

    expArray_left = bin_array_exp[:32]
    expArray_right = bin_array_exp[32:]
    exp_out_left = list(range(48))
    exp_out_right = list(range(48))
    for x in range(0,48):
        exp_out_left[x] = expArray_left[expansionSchema[x]-1]
        exp_out_right[x] = expArray_right[expansionSchema[x]-1]

    tempStr = ''
    tempStr2 = ''
    for x in range(0,len(exp_out_left)):
        tempStr = tempStr + exp_out_left[x]
        tempStr2 = tempStr2 + exp_out_right[x]
    return tempStr,tempStr2

def main():
    input_str = input("Input string: ")
    print("Hex Conversion: ",*convertHex(input_str),sep='',end='\n')
    print("Binary Conversion: ",*convertBin(input_str),sep='',end='\n')

    tempStr = ''
    for x in range(len(bin_res)):
        for y in range(len(bin_res)):
            tempStr = tempStr+bin_res[x][y]
    print(bin_res)
    permArray = ip(tempStr)
    permHex = convertBinHex(permArray)

    expPermL = expansionPerm(permArray)
    leftPerm = expPermL[0]
    rightPerm = expPermL[1]
    binExpArrL = convertBinHex(leftPerm)
    binExpArrR = convertBinHex(rightPerm)

    print("IP: ",permArray)
    print("IP Hex: ", *permHex,sep='',end='\n')
    print("Expansion Left Side: ",expPermL[0],sep='')
    print("Left Hex: ",*binExpArrL,sep='',end='\n')
    print("Expansion Right Side: ",expPermL[1],sep='')
    print("Right Hex: ",*binExpArrR,sep='',end='\n')

if __name__ == "__main__":
    main()
