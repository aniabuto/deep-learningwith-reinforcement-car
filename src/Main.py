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

    car = Car("192.168.239.249")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        car.steer(joystick.get_axis(0))

        if joystick.get_axis(5) > 0.5:
            car.accelerate()
            print("fwd")
        if joystick.get_axis(4) > 0.5:
            car.decelerate()
            print("back")
        if joystick.get_button(0):
            car.speed_break()
            print("break")
        if joystick.get_button(2):
            car.speed_break()
            print("straight")

        if joystick.get_button(1):
            car.speed_break()
            car.turn_straight()
            running = False

        car.send_data()

        # Quit Pygame
    pygame.quit()
