import requests

class Car:
    def __init__(self, ip):
        self.ipAddress = ip

        self.speed = 0
        self.speedMax = 200
        self.speedZero = 0
        self.speedMin = -200

        self.turn = 19
        self.turnMin = -9
        self.turnZero = 19
        self.turnMax = 30
        self.turnLeft = 15
        self.turnRight = 23

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

    def steer_direction(self, prediction):
        if prediction == "left":
            self.turn = self.turnLeft
        elif prediction == "right":
            self.turn = self.turnRight
        else:
            self.turn = self.turnZero

    def accelerate(self):
        self.state_changed = False
        if self.speed < self.speedMax:
            self.speed = 100#+= int(self.speedMax/10)
            self.state_changed = True

    def change_speed(self):
        self.speed = 50
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
            self.speed = -100#+= int(self.speedMin/5)
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
            self.state_changed = False

    def get_picture(self):
        url = f"http://{self.ipAddress}/photo"
        response = requests.get(url, headers=self.headers)
        # if response.status_code:
        #     name = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) + ".png"
        #     fp = open("images/" + name, 'wb')
        #     fp.write(response.content)
        #     fp.close()
        # pass
        return requests.get(url, headers=self.headers)

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
