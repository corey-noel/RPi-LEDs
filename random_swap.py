import math
import LED_control

## cycles through random colors
## swaps through colors sharply
def cycle(profile, time):
  return LED_control.random_color(int(time / profile.speed))