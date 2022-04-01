class aesClass:

    def __init__(self):
        self.value = ''
        self.hexValue = ''
        self.binValue = ''

    def getValue(self):
        return self.value

    def getHex(self):
        return self.hexValue

    def getBin(self):
        return self.binValue

    def setValue(self, inValue):
        self.value = inValue
        self.hexValue = hex(ord(inValue)).lstrip('0x').upper().zfill(2)
        self.hexToBin(self.hexValue)

    def setHex(self,inValue):
        self.hexValue = inValue
        self.hexToChar(inValue)
        self.hexToBin(inValue)

    def hexToBin(self, inValue):
        self.binValue = bin(int(inValue, 16)) [2:].zfill(8)

    def hexToChar(self, inValue):
        self.value = chr(int(inValue, 16))
