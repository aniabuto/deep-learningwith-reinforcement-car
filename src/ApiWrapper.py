import requests

class Car:
    def __init__(self, ip):
        self.ipAddress = ip

        self.speed = 0
        self.speedMax = 200
        self.speedZero = 0
        self.speedMin = -200

        self.turn = 0
        self.turnMin = -20
        self.turnZero = 0
        self.turnMax = 20

        self.state_changed = False

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

    def turn_straight(self):
        if self.turn != self.turnZero:
            self.state_changed = True
        else:
            self.state_changed = False
        self.turn = self.turnZero

    def steer(self, value):
        mapped_value = int((value + 1) * (self.turnMax - self.turnMin) / 2 + self.turnMin)
        if self.turn != mapped_value:
            self.state_changed = True
        else:
            self.state_changed = False
        self.turn = mapped_value

    def accelerate(self):
        self.state_changed = False
        if self.speed < self.speedMax:
            self.speed += int(self.speedMax/5)
            self.state_changed = True

    def speed_break(self):
        if self.speed != self.speedZero:
            self.state_changed = True
        else:
            self.state_changed = False
        self.speed = self.speedZero

    def decelerate(self):
        self.state_changed = False
        if self.speed > self.speedMin:
            self.speed += int(self.speedMin/5)
            self.state_changed = True

    def send_data(self):
        query_parameters = {
            'speed': self.speed,
            'turn': self.turn
        }
        url = f"http://{self.ipAddress}/drive"

        if self.state_changed:
            try:
                requests.get(url, params=query_parameters, headers=self.headers)
                print("sent: ", self.speed, self.turn)
            except Exception as e:
                print("failed")

    def get_picture(self):
        url = f"http://{self.ipAddress}/photo"
        requests.get(url, headers=self.headers)
        pass

    def reset(self):
        query_parameters = {
            'speed': self.speedZero,
            'turn': self.turnZero
        }
        url = f"http://{self.ipAddress}/drive"

        try:
            requests.get(url, params=query_parameters, headers=self.headers)
            print("sent: ", self.speed, self.turn)
        except Exception as e:
            print("failed")
