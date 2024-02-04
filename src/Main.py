import time


import pygame

from src.ApiWrapper import Car

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check if any joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick found.")
else:
    # Initialize the first joystick (you can choose a different index if needed)
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    car = Car("192.168.20.82")
    # car = Car("192.168.239.179")
    car.reset()

    # Main game loop
    running = True
    start = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        car.steer(joystick.get_axis(0))

        if joystick.get_axis(5) > 0.5:
            car.accelerate()
        if joystick.get_axis(4) > 0.5:
            car.decelerate()
        if joystick.get_button(0) or joystick.get_axis(5) == 0.0:
            car.speed_break()
        if joystick.get_button(2):
            car.turn_straight()

        t1 = time.time() - start
        if t1 >= 1.5:
            start = time.time()
            car.get_picture()


        if joystick.get_button(1):
            car.speed_break()
            car.turn_straight()
            running = False

        car.send_data()

        # Quit Pygame
    pygame.quit()
