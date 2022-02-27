import sacn
import time
import joystick

universe = 1000

sender = sacn.sACNsender()
sender.start()

sender.activate_output(universe)
sender[universe].multicast = False
sender[universe].destination = "127.0.0.1"
# sender[universe].destination = "10.101.200.1"

values = [0] * 4

multiplier = 0.01

joy = joystick.my_joystick()

def processValues():
  for i in range(0, len(values)):
    values[i] = min(max(-1, values[i]), 1)

def value_mapper(v):
  return round(v * 255 / 2 + 127.5)

def map_values():
  return list(map(value_mapper, values))

try:
  while True:
    joy.update()
    # print(joy.rumble(1, 1, 100))

    time.sleep(0.01)
    values[0] += multiplier * joy.get_axis("pan1")
    values[1] += multiplier * joy.get_axis("tilt1")
    values[2] += multiplier * joy.get_axis("pan2")
    values[3] += multiplier * joy.get_axis("tilt2")

    if (joy.get_button("speed_0")):
      multiplier = 0.01
    elif (joy.get_button("speed_1")):
      multiplier = 0.005
    elif (joy.get_button("speed_2")):
      multiplier = 0.001
    elif (joy.get_button("speed_3")):
      multiplier = 0.0005

    processValues()

    print(tuple(map_values()))

    sender[1000].dmx_data = tuple(map_values())
except KeyboardInterrupt:
  pass

sender.stop()
