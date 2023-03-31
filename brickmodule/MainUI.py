from tkinter import *
import os
from tkinter import filedialog
from collections import deque
from brickmodule.util import *
from brickmodule.process import *
from brickmodule.Controller import Controller
 
class Window:
    def __init__(self, master, initialText:str):
        self.master = master
        self.Main = Frame(self.master)
        self.stack = deque(maxlen = 10)
        self.stackcursor = 0
        #LABEL
        self.sequenceLabel = Label(self.Main, text = "Please load a Fasta File")
        self.sequenceLabel.pack(padx = 5, pady = 5)
        #ForbiddenList
        # Add a List Scrollbar(vertical)'
        listScrollbar=Scrollbar(self.Main, orient='vertical')
        listScrollbar.pack(side = RIGHT, fill = BOTH)
        forbiddenItems=[]
        var = Variable(value=forbiddenItems)
        self.forbiddenList = Listbox( self.Main, listvariable=var, height=1, selectmode=EXTENDED )
        forbiddenList=loadListFromFile(os.path.dirname(os.path.abspath(__file__))+"\\..\\default.txt")
        Controller.model.forbiddenList=forbiddenList
        listScrollbar.config(command = self.forbiddenList.yview)
         # Add a Scrollbar(horizontal)
        textScrollbar=Scrollbar(self.Main, orient='horizontal')
        textScrollbar.pack(side=BOTTOM, fill='x')  
        self.sequenceText = Text(self.Main, xscrollcommand=textScrollbar.set,wrap="none" )
        self.sequenceText.insert(END, initialText)
        text,label=loadTextFromFile( os.path.dirname(os.path.abspath(__file__))+"\\..\\default.fa")
        Controller.model.sequenceText=text
        Controller.model.sequenceLabel=label
        self.sequenceText.edit
        Controller.updateView(self)
        self.forbiddenList.pack(side= RIGHT, fill= BOTH)     
        self.sequenceText.pack(padx = 5, pady = 5)
        textScrollbar.config(command=self.sequenceText.xview)
        #text.pack()
        self.menu = Menu(self.Main)
        self.menu.add_command(label = "File", command = self.loadFastaFromFile)
        self.menu.add_command(label = "Print", command = self.printStack)
        self.menu.add_command(label = "Undo", command = self.undo)
        self.menu.add_command(label = "Redo", command = self.redo)
        self.menu.add_command(label = "Process Fasta", command = self.process)
        self.menu.add_command(label = "Load Forbidden List From File", command = self.loadForbiddenListFromFile)
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
        print(self.sequenceText.get("1.0", "end"))     

    def clear(self):
        self.sequenceText.delete("1.0", "end")
 
    def stackify(self):
        self.stack.append(self.sequenceText.get("1.0", "end - 1c"))
        if self.stackcursor < 9: self.stackcursor += 1
 
    def undo(self):
        if self.stackcursor != 0:
            self.clear()
            if self.stackcursor > 0: self.stackcursor -= 1
            self.sequenceText.insert("0.0", self.stack[self.stackcursor])
 
    def redo(self):
        if len(self.stack) > self.stackcursor + 1:
            self.clear()
            if self.stackcursor < 9: self.stackcursor += 1
            self.sequenceText.insert("0.0", self.stack[self.stackcursor])
 
    def printStack(self):
        i = 0
        for stack in self.stack:
            print(str(i) + " " + stack)
            i += 1
  
    def process(self):
        record:SeqRecord=loadFasta()
        process(self.sequenceText,str(record.seq),list())

    def loadFastaFromFile(self):
        fileName:str = filedialog.askopenfilename(title='Open raw Fasta File',filetypes=(('FASTA files', '*.fa'),('All files', '*.*')))
        loadTextFromFile(self.sequenceText, self.sequenceLabel, fileName)
        
    def loadForbiddenListFromFile(self):
        fileName:str = filedialog.askopenfilename(title='Open Forbidden Sequences File',filetypes=(('forbidden Item files', '*.txt'),('All files', '*.*')))
        Controller.model.forbiddenList=loadListFromFile(fileName)
        Controller.updateView(self)
        
    # end class    


def mainUI(text:str):
    root = Tk()
    root.title('Brick Designer')
    window = Window(root, text)
    root.bind("<Key>", lambda event: window.stackify())
    root.mainloop()





