import sacn
import time
import joystick
import math

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

#Clip a value to be between 0 and 1
def clip(x, minval=0, maxval=1):
  return max(minval, min(maxval, x))

#Get DMX values for a range
def getValues(value, args):
  length = math.floor((args[1] - args[0]) / args[2]) + 1
  scaled_pan = value * length/2
  values = []
  for i in range(length):
    v = 0
    if args[0]/args[2] + i < 0:
      v = clip((args[0]/args[2]) + 1 + i - scaled_pan)
    elif args[0]/args[2] + i > 0:
      v = clip(scaled_pan - ((args[0]/args[2]) - 1 + i))
    values.append(round(v*255))
  return values

# args = (min, max, inc)
pan_args = (-270, 270, 10)
tilt_args = (-140, 140, 10)

try:
  #(-1 to 1)
  pan = 0
  tilt = 0
  while True:
    joy.update()
    time.sleep(0.01)
    speed = joy.get_speed() * 0.01
    pan += joy.get_axis("pan")*speed
    tilt += joy.get_axis("tilt")*speed
    pan = clip(pan, minval=-1, maxval=1)
    tilt = clip(tilt, minval=-1, maxval=1)

    dmx = getValues(pan, pan_args)
    dmx = dmx + ([0] * (59 - len(dmx)))
    dmx += getValues(tilt, tilt_args)
    
    sender[universe].dmx_data = tuple(dmx)

    
except KeyboardInterrupt:
  pass

sender.stop()
