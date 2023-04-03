from brickmodule.Model import Model
from tkinter import END

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
        ui.master.title('Brick Designer    Sequence: '+Controller.model.sequenceLabel )
        print("view was updated from model") 



# controllerSingleton:Controller=Controller(Model(),list())


# controllerSingleton.updateView()
# controllerSingleton.model.dump()
# controllerSingleton.model.forbiddenList=["AAA","BBB"]
# controllerSingleton.model.dump()