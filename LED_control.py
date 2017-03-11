import LED 
import time 
from sys import argv 
import importlib 
import random

## members:
## refresh_time
##   speed at which LED.run_cycle() will refresh the color values of the LEDs
## speed
##   the speed at which the cycle runes
## colors[]
##   a list of colors for a cycle to use
##   can be empty
class ColorProfile:
  def __init__(self, refresh_time, speed, colors):
    self.refresh_time = refresh_time
    self.speed = speed
    self.colors = colors


## sets the color of the LED to the result of
## the function cycle once every profile.refresh_time seconds
## cycle must return a 3-tuple (r, g, b)
## values must be [0, 255]
def run_cycle(cycle, profile):
  LED.start()
  start_time = time.time()

  try:
    while True:
      curr_time = time.time()
      LED.set_color(*cycle(profile, curr_time))
      time.sleep(profile.refresh_time - ((time.time() - start_time) % profile.refresh_time))
  except (NameError, TypeError) as e:
    print(e)
    print("The module does not contain a function named cycle() that accepts a color profile and a time")
  except IndexError as e:
    print(e)
    print("Profile format does not work with cycle")
  except KeyboardInterrupt:
    pass

  LED.set_color(0, 0, 0)
  LED.stop()


## returns a random color seeded based on the time parameter
def random_color(time):
  random.seed(time)

  r = random.randint(0, 255)
  g = random.randint(0, 200)
  b = random.randint(0, 200)

  c = random.randint(0, 3)
  if c == 0:
    r = 0
  elif c == 1:
    g = 0
  elif c == 2:
    b = 0

  return (r, g, b)


## reads in the command line arguments [control_program_name] [profile_file_name]
## runs a cycle read from the control program name
## using the colors, times, and refresh rate found in the color profile file
##
## profile file format:
## [refresh time]
## [time1] [time2] ... [timen]
## [color1 in #RRGGCC hexcode format]
## [color2]
## [color3]
## ...
##
def main():
  if len(argv) < 3:
    print("Usage: python LED_control.py [control program name] [profile file name]")

  else:
    control_filename = argv[1]
    profile_filename = argv[2]
    control_module = None
    profile = None

    ## attempt to import the module containing the cycle
    try:
      control_module = importlib.import_module(control_filename)
    except ImportError as e:
      print(e)
      print("Could not find module %s!" % control_filename)

    ## attempt to read in the profile file and construct a new profile object
    try:
      refresh_time = 0
      speed = 0
      colors = []

      fv = open(profile_filename, "r")

      ## read in refresh time and speed
      times_line = fv.readline().split()
      refresh_time = float(times_line[0])
      speed = float(times_line[1])

      ## read in and parse color lines, ignoring empty lines
      line = fv.readline()
      while line != "":
        if line.strip():
          r = int(line[1:3], 16)
          g = int(line[3:5], 16)
          b = int(line[5:7], 16)
          colors.append((r, g, b))
        line = fv.readline()

      fv.close()

      profile = ColorProfile(refresh_time, speed, colors)

      print("Refresh time %f, speed %f" % (profile.refresh_time, profile.speed))
      print("Colors ", profile.colors)

    except (IOError) as e:
      print(e)
      print("Could not find file %s!" % profile_filename)
    except (ValueError, TypeError, IndexError) as e:
      print(e)
      print("File %s formatted incorrectly!" % profile_filename)

    if control_module != None and profile != None:
      run_cycle(control_module.cycle, profile)


if __name__ == "__main__":
  main()
