import sacn
import time
import joystick

universe = 200

sender = sacn.sACNsender()
sender.start()

sender.activate_output(universe)
sender[universe].multicast = False
sender[universe].destination = "10.3.8.169"
# sender[universe].destination = "10.101.200.1"

values = [0] * 29

multiplier = 0.01

joy = joystick.my_joystick()

def processValues():
  for i in range(0, len(values)):
    values[i] = min(max(-1, values[i]), 1)

def value_mapper(v):
  return round(v * 255)

def map_values():
  return list(map(value_mapper, values))

try:
  while True:
    joy.update()
    # print(joy.rumble(1, 1, 100))

    time.sleep(0.01)

    p = joy.get_axis("pan")
    t = joy.get_axis("tilt")
    values[0] = abs(p)
    values[1] = abs(t)

    speed = joy.get_speed()

    values[10] = (speed == 0 and p > 0)
    values[11] = (speed == 1 and p > 0)
    values[12] = (speed == 2 and p > 0)
    values[13] = (speed == 3 and p > 0)

    values[14] = (speed == 0 and p < 0)
    values[15] = (speed == 1 and p < 0)
    values[16] = (speed == 2 and p < 0)
    values[17] = (speed == 3 and p < 0)

    values[20] = (speed == 0 and t > 0)
    values[21] = (speed == 1 and t > 0)
    values[22] = (speed == 2 and t > 0)
    values[23] = (speed == 3 and t > 0)

    values[24] = (speed == 0 and t < 0)
    values[25] = (speed == 1 and t < 0)
    values[26] = (speed == 2 and t < 0)
    values[27] = (speed == 3 and t < 0)

    print(map_values())

    sender[universe].dmx_data = tuple(map_values())
except KeyboardInterrupt:
  pass

sender.stop()
