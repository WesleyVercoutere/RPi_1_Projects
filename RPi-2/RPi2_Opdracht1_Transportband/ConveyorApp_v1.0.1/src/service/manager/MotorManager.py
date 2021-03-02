

class MotorManager:

    def __init__(self, motor):
        self.motor = motor
        self.direction = None

    def rotate(self, direction):
        pass

    def rotateLoop(self, direction):
        self.motor.keepMoving = True
        self.direction = direction

    def stop(self):
        self.motor.keepMoving = False
        self.motor.stop()
        
    def loop(self):
        if self.motor.keepMoving:
            self.motor.rotate(self.direction)