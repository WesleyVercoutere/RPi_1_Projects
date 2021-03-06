from tkinter import Tk


class GUI:

    def __init__(self, ConveyorManager):
        self.conveyorMgr = ConveyorManager

        self.init()
        self.setLabels()

    def init(self):
        self.root = Tk()
        self.root.title('Transportband')
        self.root.geometry('800x400')

        # self.myFont = font.Font(family='Helvetica', size=40)

    def loop(self):
        self.root.mainloop()

    def setLabels(self):
        pass
        # self.label = Label(self.root, text="STANDBY", font=self.myFont, padx=20, pady=20)
        # self.label.grid(row=0, column=0)

        # self.labelTemp = Label(self.root, text="", font=self.myFont, padx=20, pady=20)
        # self.labelTemp.grid(row=0, column=1)

    def setLabelsText(self, textLabel, textTemp=""):
        self.label["text"] = textLabel
        self.labelTemp["text"] = textTemp

    def update(self, arg):
        if arg == "Toggle state":
            self.toggleState()
        
        if arg == "Update temp":
            self.updateTemp()

        if arg == "Toggle room temp":
            self.toggleRoomTemp()

        if arg == "Update room temp":
            self.toggleRoomTemp()

    def toggleState(self):
        pass
        # if self.thermostatMgr.thermostat.status:
        #     self.updateTemp()
        # else:
        #     self.setLabelsText("STANDBY")

    def updateTemp(self):
        pass
        # temp = self.thermostatMgr.thermostat.currentTemp
        # self.setLabelsText("Room temperature: ", temp)

    def toggleRoomTemp(self):
        pass
        # if self.thermostatMgr.thermostat.setRoomTemp:
        #     self.setLabelsText("Set room temperature", self.thermostatMgr.thermostat.settings.inputTemp)
        # else:
        #     self.updateTemp()
