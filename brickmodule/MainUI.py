from tkinter import *
import os
from tkinter import filedialog
from collections import deque
from brickmodule.util import *
from brickmodule.process import *
from brickmodule.Controller import Controller
from tkinter import messagebox
 
''' upon start default.fa and default.txt- with forbidden enzymes are loaded'''
#https://www.bioinformatics.org/sms2/rev_trans.html
#https://edinburgh-genome-foundry.github.io/
class Window:
    def __init__(self, master):
        self.master = master
        self.Main = Frame(self.master)
        self.stack = deque(maxlen = 10)
        self.stackcursor = 0
        #LABEL
        self.sequenceLabel = Label(self.Main, text = "Please load a Fasta File")
        self.sequenceLabel.pack(padx = 5, pady = 5)
        #ForbiddenList
        # Add a List Scrollbar(vertical)'
        # listScrollbar=Scrollbar(self.Main, orient='vertical')
        # listScrollbar.pack(side = RIGHT, fill = BOTH)
        forbiddenItems=[]
        var = Variable(value=forbiddenItems)
        # self.forbiddenList = Listbox( self.Main, listvariable=var, height=1, selectmode=EXTENDED )
        forbiddenList=loadListFromFile(os.path.dirname(os.path.abspath(__file__))+"\\..\\default.txt")
        Controller.model.forbiddenList=forbiddenList
        #listScrollbar.config(command = self.forbiddenList.yview)
         # Add a Scrollbar(horizontal)
        textScrollbar=Scrollbar(self.Main, orient='horizontal')
        textScrollbar.pack(side=BOTTOM, fill='x')  
        self.sequenceText = Text(self.Main, xscrollcommand=textScrollbar.set,wrap="none" )
        #self.sequenceText.insert(END, initialText)
        Controller.model.lastFastaFile=readLastUsedFastaFileFromFile()
        if Controller.model.lastFastaFile is not None:
            text,label=loadTextFromFile( Controller.model.lastFastaFile)
            Controller.model.sequenceText=text
            Controller.model.sequenceLabel=label
        self.sequenceText.edit
        Controller.updateView(self)
        #self.forbiddenList.pack(side= RIGHT, fill= BOTH)     
        self.sequenceText.pack(padx = 5, pady = 5,fill= BOTH)
        textScrollbar.config(command=self.sequenceText.xview)
        #text.pack()
        self.menu = Menu(self.Main)
        self.menu.add_command(label = "Load Fasta", command = self.loadFastaFromFile)
        # self.menu.add_command(label = "Print", command = self.printStack)
        # self.menu.add_command(label = "Undo", command = self.undo)
        # self.menu.add_command(label = "Redo", command = self.redo)
        self.menu.add_command(label = "Optimize", command = self.optimize)
        self.menu.add_command(label = "Show Forbidden", command = self.showForbiddenListFromFile)
        self.menu.add_command(label = "Load Forbidden", command = self.loadForbiddenListFromFile)
        self.menu.add_command(label = "Debug", command = self.debug)
        self.master.config(menu = self.menu)
 
        # self.B1 = Button(self.Main, text = "Print", width = 8, command = self.display)
        # self.B1.pack(padx = 5, pady = 5, side = LEFT)
        # self.B2 = Button(self.Main, text = "Clear", width = 8, command = self.clear)
        # self.B2.pack(padx = 5, pady = 5, side = LEFT)
        # self.B3 = Button(self.Main, text = "Undo", width = 8, command = self.undo)
        # self.B3.pack(padx = 5, pady = 5, side = LEFT)
        # self.B4 = Button(self.Main, text = "Redo", width = 8, command = self.redo)
        # self.B4.pack(padx = 5, pady = 5, side = LEFT)
        self.Main.pack(padx = 5, pady = 5, fill= BOTH)
 
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
  
    def optimize(self):
        root=self.master
        Tk.Entry(root).grid()   # something to interact with
        def dismiss ():
            dlg.grab_release()
            dlg.destroy()

        dlg = Toplevel(root)
        Tk.Button(dlg, text="Done", command=dismiss).grid()
        dlg.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
        dlg.transient(root)   # dialog window is related to main
        dlg.wait_visibility() # can't grab until window appears, so we wait
        dlg.grab_set()        # ensure all input goes to our window
        dlg.wait_window()     # block until window is destroyed
        optimize(self.sequenceText,Controller.model.sequenceText)

    def loadFastaFromFile(self):
        fileName:str = filedialog.askopenfilename(title='Open raw Fasta File',filetypes=(('FASTA files', '*.fa'),('All files', '*.*')))
        text,label=loadTextFromFile( fileName)
        Controller.model.sequenceText=text
        Controller.model.sequenceLabel=label
        Controller.model.lastFastaFile=fileName
        Controller.updateView(self)
         
    def loadForbiddenListFromFile(self):
        fileName:str = filedialog.askopenfilename(title='Open Forbidden Sequences File',filetypes=(('forbidden Item files', '*.txt'),('All files', '*.*')))
        Controller.model.forbiddenList=loadListFromFile(fileName)
        Controller.updateView(self)
        self.showForbiddenListFromFile()

    def showForbiddenListFromFile(self):
        listString=""
        for line in Controller.model.forbiddenList:
            listString+=line
        messagebox.showinfo("Forbidden list", listString+"                    ")

    def debug(self):
        print("Model")
        Controller.model.dump()
        messagebox.showinfo("Model", Controller.model.dump())
        
    # end class    


def mainUI(text:str):
    root = Tk()
    root.title('Brick Designer')
    root.geometry(str(root.winfo_screenwidth())+"x"+str( int(root.winfo_screenheight()*.7)))
    #root.state('zoomed')
    window = Window(root)
    #root.attributes('-fullscreen', True)
    #screen_width = win.winfo_screenwidth()
    root.bind("<Key>", lambda event: window.stackify())
    root.protocol( "WM_DELETE_WINDOW", onExit )
    root.mainloop()


def onExit():
     #messagebox.showinfo("bye", "bye")
     saveLastFastaFileToFile(Controller.model.lastFastaFile)
     #os.path.dirname(os.path.abspath(__file__))+"\\..\\default.fa"
     quit()


