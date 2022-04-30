import sacn
import time
import joystick
import math

universe = 200

sender = sacn.sACNsender()
sender.start()

sender.activate_output(universe)
sender[universe].multicast = False
# sender[universe].destination = "10.3.254.2"
sender[universe].destination = "10.101.200.1"

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

def addDMX(dmx, startAddress, values):
  for i in range(0, len(values)):
    dmx[i + startAddress - 1] = values[i]

# args = (min, max, inc, dmx)
pan_args = (-270, 270, 10, 1)
tilt_args = (-140, 140, 10, 60)
iris_args = (0, 75, 75, 98)

try:
  #(-1 to 1)
  pan = 0
  tilt = 0
  #(0 to 1)
  iris = 1
  irisInertia = 0
  while True:
    joy.update()
    time.sleep(0.01)
    speed = joy.get_speed() * 0.01
    pan += joy.get_axis("pan")*speed
    tilt += joy.get_axis("tilt")*speed
    if joy.get_hat()[1] > 0:
      if irisInertia <= 0:
        irisInertia = 1
      irisInertia += 0.15
    elif joy.get_hat()[1] < 0:
      if irisInertia >= 0:
        irisInertia = -1
      irisInertia -= 0.15

    else:
      irisInertia = 0
    iris += irisInertia*0.0005
    pan = clip(pan, minval=-1, maxval=1)
    tilt = clip(tilt, minval=-1, maxval=1)
    iris = clip(iris, minval=0, maxval=1)


    dmx = [0] * 100
    addDMX(dmx, 1, [1, 2, 3])
    addDMX(dmx, pan_args[3], getValues(pan, pan_args))
    addDMX(dmx, tilt_args[3], getValues(tilt, tilt_args))
    addDMX(dmx, iris_args[3], [round((1 - iris)*255)])
    # print(dmx)

    sender[universe].dmx_data = tuple(dmx)

    
except KeyboardInterrupt:
  pass

sender.stop()
