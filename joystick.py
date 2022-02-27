import pygame
pygame.init()

c = pygame.joystick.get_count()
if c < 1:
    print("No joystick found!")
    exit(-1)
elif c > 1:
    print(f"Warning: {c} joysticks found, using the first one.")

class my_joystick:
  joy_axes = {
    "pan1": 0,
    "tilt1": 1,
    "pan2": 2,
    "tilt2": 4
  }

  joy_buttons = {
    "speed_0": 0,
    "speed_1": 1,
    "speed_2": 2,
    "speed_3": 3,
  }

  def __init__(self):
    self.joy = pygame.joystick.Joystick(0)
    self.joy.init()
  
  def update(self):
    pygame.event.pump()

  def get_axis(self, name):
    return self.joy.get_axis(self.joy_axes[name])
  
  def get_button(self, name):
    return self.joy.get_button(self.joy_buttons[name])

