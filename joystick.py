import pygame
pygame.init()

c = pygame.joystick.get_count()
if c < 1:
    print("No joystick found!")
    exit(-1)
elif c > 1:
    print(f"Warning: {c} joysticks found, using the first one.")

class my_joystick:
  # joy_axes = {
  #   "pan1": 0,
  #   "tilt1": 1,
  #   "pan2": 2,
  #   "tilt2": 4
  # }

  joy_axes = {
    "pan": 2,
    "tilt": 1,
    "speed": 3
  }

  def get_speed(self):
    if self.get_axis("speed") > 0.5:
      return 3
    elif self.get_axis("speed") > 0:
      return 2
    elif self.get_axis("speed") > -0.5:
      return 1
    else:
      return 0

  def __init__(self):
    self.joy = pygame.joystick.Joystick(0)
    self.joy.init()
  
  def update(self):
    pygame.event.pump()

  def get_axis(self, name):
    return -self.joy.get_axis(self.joy_axes[name])
  
  def get_button(self, name):
    return self.joy.get_button(self.joy_buttons[name])

