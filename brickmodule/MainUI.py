from tkinter import *
import os
from tkinter import filedialog
from collections import deque
from brickmodule.util import *
 
class Window:
    def __init__(self, master, initialText:str):
        self.master = master
        self.Main = Frame(self.master)
        self.stack = deque(maxlen = 10)
        self.stackcursor = 0
        #LABEL
        self.label = Label(self.Main, text = "Brick Designer Label")
        self.label.pack(padx = 5, pady = 5)
        #ForbiddenList
         # Add a List Scrollbar(vertical)'
        listScrollbar=Scrollbar(self.Main, orient='vertical')
        listScrollbar.pack(side = RIGHT, fill = BOTH)
        forbiddenItems=[]
        var = Variable(value=forbiddenItems)
        self.forbiddenList = Listbox( self.Main, listvariable=var, height=1, selectmode=EXTENDED )
        loadListFromFile(self.forbiddenList,os.path.dirname(os.path.abspath(__file__))+"\\..\\default.txt")
        listScrollbar.config(command = self.forbiddenList.yview)
        self.forbiddenList.pack(side= RIGHT, fill= BOTH)     
        #
         # Add a Scrollbar(horizontal)
        textScrollbar=Scrollbar(self.Main, orient='horizontal')
        textScrollbar.pack(side=BOTTOM, fill='x')  
        self.infoText = Text(self.Main, xscrollcommand=textScrollbar.set,wrap="none" )
        self.infoText.insert(END, initialText)
        self.infoText.edit
        self.infoText.pack(padx = 5, pady = 5)
        textScrollbar.config(command=self.infoText.xview)
        #text.pack()
        self.menu = Menu(self.Main)
        self.menu.add_command(label = "File", command = self.loadFile)
        self.menu.add_command(label = "Print", command = self.printStack)
        self.menu.add_command(label = "Undo", command = self.undo)
        self.menu.add_command(label = "Redo", command = self.redo)
        self.menu.add_command(label = "setText", command = self.setText)
        self.menu.add_command(label = "loadForbiddenListFromFile", command = self.loadForbiddenListFromFile)
        self.master.config(menu = self.menu)
 
        self.B1 = Button(self.Main, text = "Print", width = 8, command = self.display)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)
        self.B2 = Button(self.Main, text = "Clear", width = 8, command = self.clear)
        self.B2.pack(padx = 5, pady = 5, side = LEFT)
        self.B3 = Button(self.Main, text = "Undo", width = 8, command = self.undo)
        self.B3.pack(padx = 5, pady = 5, side = LEFT)
        self.B4 = Button(self.Main, text = "Redo", width = 8, command = self.redo)
        self.B4.pack(padx = 5, pady = 5, side = LEFT)
        self.Main.pack(padx = 5, pady = 5)
 
    def display(self):
        print(self.infoText.get("1.0", "end"))     

    def clear(self):
        self.infoText.delete("1.0", "end")
 
    def stackify(self):
        self.stack.append(self.infoText.get("1.0", "end - 1c"))
        if self.stackcursor < 9: self.stackcursor += 1
 
    def undo(self):
        if self.stackcursor != 0:
            self.clear()
            if self.stackcursor > 0: self.stackcursor -= 1
            self.infoText.insert("0.0", self.stack[self.stackcursor])
 
    def redo(self):
        if len(self.stack) > self.stackcursor + 1:
            self.clear()
            if self.stackcursor < 9: self.stackcursor += 1
            self.infoText.insert("0.0", self.stack[self.stackcursor])
 
    def printStack(self):
        i = 0
        for stack in self.stack:
            print(str(i) + " " + stack)
            i += 1
  
    def setText(self):
        self.infoText.insert(END, "SOme text")


    def loadFile(self):
        #filename:str = filedialog.askopenfilename(title='Open raw Fasta File', initialdir='/',filetypes=(('text files', '*.txt'),('All files', '*.*')))
        filename:str = filedialog.askopenfilename(title='Open raw Fasta File',filetypes=(('FASTA files', '*.fa'),('All files', '*.*')))
        record=loadFasta(filename)
        newText= 'id {id} {len} {sequence}'.format(id =record.id, len=len(record), sequence=record.seq )
        print("newText:" +newText)
        self.infoText.insert(END,"\n"+newText) # replace can also be used
        
    def loadForbiddenListFromFile(self):
        fileName:str = filedialog.askopenfilename(title='Open Forbidden Sequences File',filetypes=(('forbidden Item files', '*.txt'),('All files', '*.*')))
        loadListFromFile(self.forbiddenList,fileName)
        
    # end class    


def mainUI(text:str):
    root = Tk()
    root.title('Brick Designer')
    window = Window(root, text)
    root.bind("<Key>", lambda event: window.stackify())
    root.mainloop()





