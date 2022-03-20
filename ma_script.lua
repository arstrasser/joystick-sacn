local numdmxremote = 1

function createExec(execNum)
  gma.cmd("Store Exec "..execNum)
  gma.cmd("Assign TempFader Exec "..execNum)
end

function generateExecsAndRemotes(attribute, min, max, inc, execNumStart, execPage, dmxUniverse) 
  gma.cmd("Off Attribute *")
  local cur = min
  local execNum = execNumStart
  while (cur <= max)
  do
    gma.cmd("Attribute "..attribute.." At "..cur)
    createExec(execNum)
    gma.cmd("Assign Remote 3."..numdmxremote.." /name=\"JOYSTICKCONTROL\" /type=exec /page="..execPage.." /executor="..execNum.. " /button=3 /dmx="..dmxUniverse.."."..execNum)
    numdmxremote = numdmxremote + 1
    execNum = execNum + 1
    cur = cur + inc
  end
end

function generateFaderPages(numpages) 
  for i = 1, 100 do
    gma.cmd("Page 1."..i)
  end
end

function JoystickSetup(number)
  generateFaderPages()

  if number == 0 then
    --Delete Execs
    gma.cmd("Page 1.101")
    gma.cmd("Delete Exec 1 Thru")
    gma.cmd("Page 1.102")
    gma.cmd("Delete Exec 1 Thru")

    --Delete all DMX Remotes
    gma.cmd("Delete Remote 3.1 Thru")
    numdmxremote = 1

    gma.feedback("Reset joysticks")
  elseif number == 1 then
    gma.cmd("Page 1.101")
    generateExecsAndRemotes("pan", -270, 270, 10, 1, 101, 200)
    generateExecsAndRemotes("tilt", -140, 140, 10, 60, 101, 200)
    generateExecsAndRemotes("iris", 0, 75, 75, 98, 101, 200)
    gma.cmd("Off Attribute *")
    gma.cmd("Page 1.1")
  elseif number == 2 then
    gma.cmd("Page 1.102")
    generateExecsAndRemotes("pan", -270, 270, 10, 1, 102, 201)
    generateExecsAndRemotes("tilt", -140, 140, 10, 60, 102, 201)
    generateExecsAndRemotes("iris", 0, 75, 75, 98, 102, 201)
    gma.cmd("Off Attribute *")
    gma.cmd("Page 1.1")
  else
    gma.feedback("ERROR: must specify a joystick number of either 1 or 2")
  end
end

function main() 
  gma.feedback("Call these lua functions from macros!")
  gma.feedback("Credit: Alex Strasser (CMU 2023)")
end


return main;