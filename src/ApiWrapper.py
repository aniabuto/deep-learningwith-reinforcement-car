import requests

class Car:
    def __init__(self, ip):
        self.ipAddress = ip

        self.speed = 0
        self.speedMax = 255
        self.speedZero = 0
        self.speedMin = -255

        self.turn = 0
        self.turnMin = -20
        self.turnZero = 0
        self.turnMax = 20

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

    def turn_left(self):
        if self.turn > self.turnMin:
            self.turn -= 1

    def turn_straight(self):
        self.turn = self.turnZero
        self.send_data()

    def turn_right(self):
        if self.turn < self.turnMax:
            self.turn += 1

    def steer(self, value):
        # Map the input_value to the [a, b] range
        mapped_value = int((value + 1) * (self.turnMax - self.turnMin) / 2 + self.turnMin)
        print(value, mapped_value)
        self.turn = mapped_value
        self.send_data()

    def accelerate(self):
        if self.speed < self.speedMax:
            self.speed += 85
        self.send_data()

    def speed_break(self):
        self.speed = self.speedZero
        self.send_data()

    def decelerate(self):
        if self.speed > self.speedMin:
            self.speed -= 85
        self.send_data()

    def send_data(self):
        # TODO: add sending request of (speed, turn) to given IP
        query_parameters = {
            'speed': self.speed,
            'turn': self.turn
        }
        url = f"http://{self.ipAddress}/drive"
        # while True:
        try:
            requests.get(url, params=query_parameters, headers=self.headers)
        except Exception as e:
            print("failed")


        # if response.status_code == 200:
        #     print(query_parameters)
        #     print("Request was successful.")
        #     print("Response content:", response.text)
        # else:
        #     print(f"Request failed with status code {response.status_code}: {response.text}")
        # pass

    def get_picture(self):
        # TODO: add getting picture from given IP
        url = f"http://{self.ipAddress}/photo"
        requests.get(url, headers=self.headers)
        pass
