from domain import ConveyorState, PositionState
from hardware import Rotation
from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, conveyor,
                 inputManager,
                 ledManager,
                 motorManager,
                 displayManager,
                 positionManager):
        super(ConveyorManager, self).__init__()

        self.conveyor = conveyor
        self.inputMgr = inputManager
        self.ledMgr = ledManager
        self.motorMgr = motorManager
        self.displayMgr = displayManager
        self.positionMgr = positionManager

        self.inputMgr.setConveyor(self)
        self.startHoming()

    def startHoming(self):
        self.setConveyorProperties(False, ConveyorState.MOVING_TO_HOME_POSITION, PositionState.NONE)
        self.motorMgr.rotate(Rotation.COUNTERCLOCKWISE)
        self.ledMgr.updateSignal(self.conveyor)

    def moveOneStep(self, direction):
        pass

    def moveToPosition(self, position):
        pass

    def setConveyorProperties(self, isHomed, conveyorState, positionState):
        self.conveyor.isHomed = isHomed
        self.conveyor.state = conveyorState
        self.conveyor.position = positionState

    def loop(self):
        while True:
            self.inputMgr.loop()
            self.ledMgr.loop()
            self.motorMgr.loop()
            self.displayMgr.loop()
