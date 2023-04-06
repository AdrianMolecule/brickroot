import brickpackage.Model
from tkinter import END
from brickpackage.Model import Model

class Controller:

    model:Model=Model()
    view=None
    # def __init__(self, model, view):
    #     self.model:Model=model
    #     self.view=view

    def updateView(ui):
        # ui.forbiddenList.delete(0,END)
        # for line in Controller.model.forbiddenList:
        #     ui.forbiddenList.insert(END,line)
        #     ui.sequenceText.delete("1.0", "end")
        ui.clear()
        ui.sequenceText.insert(END,"\n"+ "" if Controller.model.sequenceText is None else Controller.model.sequenceText) # replace can also be used
        ui.sequenceLabel['text'] =Controller.model.sequenceLabel # replace can also be used
        if(Controller.model.sequenceLabel!=None):
            ui.master.title('Brick Designer    Sequence:'+Controller.model.sequenceLabel)
        else:
            ui.master.title('Brick Designer ')        
        print("view was updated from model") 


