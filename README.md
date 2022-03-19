# Joystick to SACN
Created by Alex Strasser at Carnegie Mellon University AB Tech

## Description
This script runs on a computer using python, and forwards values from a joystick over sacn to the GrandMA 2. There are two main components to this project: the grandMA side, and the python side. The python side connects to a joystick using the pygame library, then converting those values to dmx and sending them over sacn. The grandMA side has a lua plugin which generates tempfaders for the currently selected lights. It then sets up DMX remotes to map the sacn dmx values to those tempfaders. 

## Files
 - `ma_script.lua` - Contains all of the grandMA plugin code. The main code is in the `JoystickSetup` function, which can be called with different values. When called with a value of `0`, it clears all of the joystick setups. When called with a value of `1` or `2` it sets up the first or second joystick with the currently selected lights. Note that this should not be done live during the show as it will clear the currently selected lights' attributes.
 - `main.py` - Contains the main python code for sending joystick to sacn. Currently, only one joystick is supported, but this file could be extended.
 - `joystick.py` - Contains helper functions for remapping some of the weird default pygame joystick behavior.
 - `sample.lua` - Contains the sample lua code provided by the grandMA board with a list of possible functions.
 - `joystick_tester.py` - Code to help identify the axis and button numbers on a joystick.