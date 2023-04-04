
from tkinter import *
from brickmodule.Controller import Controller
class OptimizeDialog:
    def __init__(self, parent, title, labeltext = '' ):
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry(str(int(parent.winfo_screenwidth()*.4))+"x"+str( int(parent.winfo_screenheight()*.5)))
        if len(title) > 0: self.top.title(title)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        #self.top.pack(fill=BOTH, expand=1)
        minGcContentLabel=Label(self.top, text="min GC Content")
        minGcContentLabel.grid(row=0, column=0,columnspan=2, sticky ="N", padx=5, pady=1)
        maxGcContentLabel=Label(self.top, text="max GC Content")
        maxGcContentLabel.grid(row=1, column=0,columnspan=2, sticky ="N", padx=5, pady=1)
        if(Controller.model.minGcContent!=None and Controller.model.maxGcContent!=None):
            self.minGcContentText = Entry(self.top,text=str(Controller.model.minGcContent) ,width=20)
            self.maxGcContentText = Entry(self.top,text=str(Controller.model.maxGcContent) ,width=20)
        else:
            self.minGcContentText = Entry(self.top ,width=10)
            self.maxGcContentText = Entry(self.top ,width=10)
        self.minGcContentText.grid(row=0, column=2, sticky ="N", padx=10, pady=1)
        self.maxGcContentText.grid(row=1, column=2, sticky ="N", padx=10, pady=1)
        
        okButton = Button(self.top, text="OK", command=self.ok)
        okButton.grid(row=10, column=2, sticky ="S", padx=10, pady=20)
        #ForbiddenList
        forbiddenListLabel=Label(self.top, text="Forbidden cut sites")
        var = Variable(value=Controller.model.forbiddenList)
        forbiddenList = Listbox(self.top, listvariable=var, height=10, selectmode=EXTENDED )
        # Add a List Scrollbar(vertical)'
        listScrollbar=Scrollbar(forbiddenList, orient='vertical')
        #listScrollbar.pack(side = RIGHT, fill = BOTH)
        listScrollbar.config(command = forbiddenList.yview)
        forbiddenListLabel.grid(row=0, column=3,columnspan=1, padx=10, pady=1)
        forbiddenList.grid(row=1, column=3,columnspan=20,  padx=10, pady=1)
        self.top.bind("<Return>", self.ok)
        # #self.e = Entry(self.top, text="XXX")
        self.top.bind("<Escape>", self.cancel)
        self.top.focus_set()
        parent.pack( padx=10, pady=10,fill= NONE)
        #self.top.pack()
        #self.top.grid(row=0, column=0)
        #self.top.pack(padx = 5, pady = 5, fill=NONE) #, )
 
    def ok(self, event=None):
        Controller.model.minGcContent=float(self.minGcContentText.get())
        Controller.model.maxGcContent=float(self.maxGcContentText.get())
        print ("OK")
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()