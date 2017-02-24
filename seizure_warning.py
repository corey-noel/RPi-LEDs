import LED
import random

## S U F F E R I N G

def seizure_cycle():
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  return (red, green, blue)


## note the sleep_time of .2 (default is .05)
LED.run_cycle(seizure_cycle, .2)