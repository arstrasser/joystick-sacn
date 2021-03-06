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

  joy_buttons = {
    "trigger": 1
  }

  def __init__(self):
    self.joy = pygame.joystick.Joystick(0)
    self.joy.init()
  
  def update(self):
    pygame.event.pump()

  def get_axis(self, name):
    eps = 0.01
    value = self.joy.get_axis(self.joy_axes[name])
    if abs(value) < eps:
      value = 0
    return value
  
  def get_button(self, name):
    return self.joy.get_button(self.joy_buttons[name])
  
  def get_hat(self):
    return self.joy.get_hat(0)

  def get_speed(self):
    return ((1+self.get_axis("speed")) / 2)**2

