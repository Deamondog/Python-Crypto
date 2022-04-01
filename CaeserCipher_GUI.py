import tkinter as tk

class ceaser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ceaser Cipher")

        #encode_button = 
        tk.Button(self,text="Encode",command=lambda:self.getInput(1)).grid(row=0,column=0,padx=(5,2),pady=5,sticky="NW")
        #decode_button = 
        tk.Button(self,text="Decode",command=lambda:self.getInput(2)).grid(row=1,column=0,padx=(5,2),pady=5,sticky="NW")
        #close_button = 
        tk.Button(self,text="Close",command=self.destroy).grid(row=0,column=1,padx=(5,2),pady=5,sticky="NE")

        self.shift_var=tk.StringVar(self,value='0')
        self.shift_var.trace_variable("w",self.on_write)
        self.shiftNum = tk.Entry(self,textvar=self.shift_var,width=2)
        self.shiftNum.grid(row=0,column=0,padx=145,pady=7,sticky="NW")

        self.shift_lbl = tk.Label(text="Shift Number:",height=1).grid(row=0,column=0,padx=60,pady=7,sticky="NW")


        self.inputtxt = tk.Text(self, height=30,width=50,bg='SeaGreen')
        self.inputtxt.grid(row=3,column=0,padx=5,pady=(5,10),sticky="NW")

        self.outputtxt = tk.Text(self, height=30, width=50,bg='AntiqueWhite1')
        self.outputtxt.grid(row=3,column=1,padx=5,pady=(5,10),sticky="NW")




    def encodetxt(self,text,shift):
        text = text.upper()
        newText=''
        for x in range(len(text)):
            if text[x].isalpha():
                newText += chr((ord(text[x]) + shift-65) % 26 + 65)
            else:
                newText = newText[:x] + " " + newText[x:]
        return newText

    def decrypt(self,text,shift):
        l1=[]
        if shift > 0:
            shift = 26-shift
            decryptText = self.encodetxt(text,shift)
            return decryptText
        else:
            for x in range(26):
                decryptText = self.encodetxt(text,x)
                l1.append(str(x)+':'+decryptText)
            return '\n'.join(l1)

    def getInput(self,args):
        shift = self.shift_var.get()
        text = self.inputtxt.get('1.0','end-1c')
        if args == 1:
            encoded=self.encodetxt(text,int(shift))
            self.printText(encoded)

        if args == 2:
            decoded=self.decrypt(text,int(shift))
            self.printText(decoded)

    def printText(self,text):
        self.outputtxt.config(state='normal')
        self.outputtxt.delete(1.0,'end')
        self.outputtxt.insert('end',text)
        self.outputtxt.config(state='disabled')

    def on_write(self,*args):
        try:
            int(self.shiftNum.get())
            if len(self.shift_var.get()) >2:
                self.shift_var.set(self.shift_var.get()[:2])
        except ValueError:
            self.shiftNum.delete(0,'end')


if __name__ == '__main__':
    win = ceaser()
    win.mainloop()
