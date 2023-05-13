import brickpackage.Model
from tkinter import END
from brickpackage.Model import Model
from brickpackage.Util import Util

class Controller:

    model:Model=Model()
    view=None
    # def __init__(self, model, view):
    #     self.model:Model=model
    #     self.view=view

    def updateView(ui):
        # ui.forbiddenList.delete(0,"end")
        # for line in Controller.model.forbiddenList:
        #     ui.forbiddenList.insert("end",line)
        #     ui.sequenceText.delete("1.0", "end")
        ui.clear()
        ui.sequenceLabel['text'] =Controller.model.sequenceLabel # replace can also be used
        text="" if Controller.model.sequenceText is None else Controller.model.sequenceText
        Util.appendDnaLineWithHighlightedCodons(ui.sequenceTextBox, text)
    
        # ui.sequenceText.insert(END,"\n"+ "" if Controller.model.sequenceText is None else Controller.model.sequenceText) # replace can also be used
        # ui.sequenceText.tag_config("start", background="white", foreground="blue")
        # text:str=ui.sequenceText.get("1.0", "end") 
        # for co in range(0,len(text),6):
        #     ui.sequenceText.tag_add("start", "1."+str(co), "1."+str(co+3))

        if(Controller.model.sequenceLabel!=None):
            ui.master.title('Brick Designer    Sequence:'+Controller.model.sequenceLabel)
        else:
            ui.master.title('Brick Designer ')        
        print("view was updated from model") 


