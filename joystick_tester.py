import pygame
import time

pygame.init()

c = pygame.joystick.get_count()
if c < 1:
  print("No joystick found!")
  exit(-1)
elif c > 1:
  print(f"Warning: {c} joysticks found, using the first one.")

joy = pygame.joystick.Joystick(0)
joy.init()

while True:
  pygame.event.pump()
  axes = ""
  for a in range(joy.get_numaxes()):
    axes += str(joy.get_axis(a))+"\t"
  # print("Axes:\t"+axes)

  buttons = ""
  for b in range(joy.get_numbuttons()):
    buttons += str(joy.get_button(b))+"\t"
  # print("Btns:\t"+buttons)
  print(joy.get_hat(0))

  time.sleep(0.1)