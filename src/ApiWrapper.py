class Car:
    def __init__(self, ip):
        self.ipAddress = ip

        self.speed = 0
        self.speedMax = 255
        self.speedZero = 0
        self.speedMin = -255

        self.turn = 8
        self.turnMin = -20
        self.turnZero = 0
        self.turnMax = 20

    def turn_left(self):
        if self.turn > self.turnMin:
            self.turn -= 1

    def turn_straight(self):
        self.turn = self.turnZero

    def turn_right(self):
        if self.turn < self.turnMax:
            self.turn += 1

    def accelerate(self):
        if self.speed < self.speedMax:
            self.speed += 1

    def speed_break(self):
        self.speed = self.speedZero

    def decelerate(self):
        if self.speed > self.speedMin:
            self.speed -= 1

    def send_data(self):
        # TODO: add sending request of (speed, turn) to given IP
        pass

    def get_picture(self):
        # TODO: add getting picture from given IP
        pass
