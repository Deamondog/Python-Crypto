from aesClass import *
from tkinter import *

class AES():
    def __init__(self):
        self.wordToEncrypt=''
        self.elementList = []
        self.cipherKeyLst = []

        self.input_str()
        self.cipher_key()
        self.myWindow = Tk()
        self.printWin(self.myWindow, 'AES',self.elementList,0,'State')
        self.printWin(self.myWindow, 'AES',self.cipherKeyLst,5,'Cihper Key')
        self.demoSBox(self.elementList)

    def printWin(self, myWindow, inTitle,inLst,startRow,title):
        myWindow.title(inTitle)
        lst = []
        for x in range(16):
            lst.append(inLst[x].getHex())
        print(lst)
        rows = 4
        cols = 5
        count=0
        l1 = Label(myWindow, text = title)
        l1.grid(row = startRow, column = 0, sticky = W, pady =2)
        startRow += 1
        for i in range(1,cols):
            for j in range(startRow, startRow+rows):
                self.e = Entry(myWindow, width=4)
                self.e.grid(row=j,column=i,padx=1,pady=1,ipadx=5,ipady=5)
                self.e.insert(END,"   "+lst[count])
                count +=1


    def cipher_key(self):
        lst = ["45","AD","1E","8F","9C","34","9A", "BE", "2F", "16","4C","25","67","AB","1C","7A"]

        for i in lst:
            element = aesClass()
            element.setHex(i)
            self.cipherKeyLst.append(element)

        for ele in range(len(self.elementList)):
            print("Cipher Hex:", self.elementList[ele].getHex())

    def input_str(self):
        self.wordToEncrypt = '7O845yoLHf610qmK'
        for ch in self.wordToEncrypt:
            element = aesClass()
            element.setValue(ch)
            self.elementList.append(element)

        for ele in range(len(self.elementList)):
            print("Word Hex: ", self.elementList[ele].getHex())

    def demoSBox(self,inList):
        for x in range(len(inList)):
            print(self.replaceUsingSBox(inList[x].getHex()))


    def replaceUsingSBox(self,inValue):
        sValues = {'00':'63','01':'7C','02':'77','03':'7B','04':'F2','05':'6B','06':'6F','07':'C5','08':'30','09':'01','0A':'67','0B':'2B','0C':'FE','0D':'D7','0E':'AB','0F':'76',\
                '10':'CA','11':'82','12':'C9','13':'7D','14':'FA','15':'59','16':'47','17':'F0','18':'AD','19':'D4','1A':'A2','1B':'AF','1C':'9C','1D':'A4','1E':'72','1F':'C0',\
                '20':'B7','21':'FD','22':'93','23':'26','24':'36','25':'3F','26':'F7','27':'CC','28':'34','29':'A5','2A':'E5','2B':'F1','2C':'71','2D':'D8','2E':'31','2F':'15',\
                '30':'04','31':'C7','32':'23','33':'C3','34':'18','35':'96','36':'05','37':'9A','38':'07','39':'12','3A':'80','3B':'E2','3C':'EB','3D':'27','3E':'B2','3F':'75',\
                '40':'09','41':'83','42':'2C','43':'1A','44':'1B','45':'6E','46':'5A','47':'A0','48':'52','49':'3B','4A':'D6','4B':'B3','4C':'29','4D':'E3','4E':'2F','4F':'84',\
                '50':'53','51':'D1','52':'00','53':'ED','54':'20','55':'FC','56':'B1','57':'5B','58':'6A','59':'CB','5A':'BE','5B':'39','5C':'4A','5D':'4C','5E':'58','5F':'CF',\
                '60':'D0','61':'EF','62':'AA','63':'FB','64':'63','65':'4D','66':'33','67':'85','68':'45','69':'F9','6A':'02','6B':'7F','6C':'50','6D':'3C','6E':'9F','6F':'A8',\
                '70':'51','71':'A3','72':'40','73':'8F','74':'92','75':'9D','76':'38','77':'F5','78':'BC','79':'B6','7A':'DA','7B':'21','7C':'10','7D':'FF','7E':'F3','7F':'D2',\
                '80':'CD','81':'0C','82':'13','83':'EC','84':'5F','85':'97','86':'44','87':'17','88':'C4','89':'A7','8A':'7E','8B':'3D','8C':'64','8D':'5D','8E':'19','8F':'73',\
                '90':'60','91':'81','92':'4F','93':'DC','94':'22','95':'2A','96':'90','97':'88','98':'46','99':'EE','9A':'B8','9B':'14','9C':'DE','9D':'5E','9E':'0B','9F':'DB',\
                'A0':'E0','A1':'32','A2':'3A','A3':'0A','A4':'49','A5':'06','A6':'24','A7':'5C','A8':'C2','A9':'D3','AA':'AC','AB':'62','AC':'91','AD':'95','AE':'E4','AF':'79',\
                'B0':'E7','B1':'C8','B2':'37','B3':'6D','B4':'8D','B5':'D5','B6':'4E','B7':'A9','B8':'6C','B9':'56','BA':'F4','BB':'EA','BC':'65','BD':'7A','BE':'AE','BF':'08',\
                'C0':'BA','C1':'78','C2':'25','C3':'2E','C4':'1C','C5':'A6','C6':'B4','C7':'C6','C8':'E8','C9':'DD','CA':'74','CB':'1F','CC':'4B','CD':'BD','CE':'8B','CF':'8A',\
                'D0':'70','D1':'3E','D2':'B5','D3':'66','D4':'48','D5':'03','D6':'F6','D7':'0E','D8':'61','D9':'35','DA':'57','DB':'B9','DC':'86','DD':'C1','DE':'1D','DF':'9E',\
                'E0':'E1','E1':'F8','E2':'98','E3':'11','E4':'69','E5':'D9','E6':'8E','E7':'94','E8':'9B','E9':'1E','EA':'87','EB':'E9','EC':'CE','ED':'55','EE':'28','EF':'DF',\
                'F0':'8C','F1':'A1','F2':'89','F3':'0D','F4':'BF','F5':'E6','F6':'42','F7':'68','F8':'41','F9':'99','FA':'2D','FB':'0F','FC':'B0','FD':'54','FE':'BB','FF':'16'}
        return sValues[inValue]

    # def roundKey(self):
    #     print("todo")
    # def shiftUp(self,inList):

    #     self.newList = []
    #     for x in range(12,16):
    #         self.newList.append(inList[x])



    # def createRoundKey(self):
    #     self.cKlastColumn= []
    #     self.cKlastColumn.append(self.cipherKeyLst[12])
    #     self.cKlastColumn.append(self.cipherKeyLst[13])
    #     self.cKlastColumn.append(self.cipherKeyLst[14])
    #     self.cKlastColumn.append(self.cipherKeyLst[15])
    #     self.updatedList = self.shiftUp(self.cKlastColumn)
    #     for x in range(len(self.updatedList)):
    #         self.updatedList[x].setHex(self.replaceUsingSBox(self.updatedList[x].getHex()))
    #
    #     self.newlstCol = []
    #     for x in range(4):
    #         newHexVal = aesClass()
    #         nexHexVal = self.xor(self.updatedList[x], self.cipherKeyLst[x])
    #         print ("\n", newHexVal)
    #         self.newlstCol.append(newHexVal.replace('0x','').upper().zfill(2))
    #     self.newlstCol[0]=hex(int(self.newlstCol[0]),16^int('01',16)).lstrip('0x').upper().zfill(2)
    #     self.roundKeyCol1 = self.newlstCol
    #     tempCol=[]
    #     for x in range(4,8):
    #         tempCol.append(self.cipherKeyList[x].getHex())
    #     self.roundKeyCol2 = self.xorCol(self.roundKeyCol1, tempCol)
    #     print('Col1',self.roundKeyCol1)
    #     print('Col2',self.roundKeyCol2)
    #
    # def xor(self, inVal1, inVal2):
    #     return hex(int(inVal1.getHex(),16)^int(inVal2.getHex(),16))
    #
    #
    # def shiftUp(self,inList):
    #     temp = inList[0]
    #     for x in range(len(inList)-1):
    #         inList[x] = inList[x+1]
    #     inList[len(inList)-1] = temp
    #     return inList

AES().mainloop()
# def main():
#     AES()
#
# if __name__ == "__main__":
#     main()
