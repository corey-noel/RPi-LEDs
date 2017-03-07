import math
import LED_control

## fades a random color in and then out
def cycle(profile, time):
  curr_color = LED_control.random_color(int(time / profile.speed))
  curr_strength = (math.cos(2 * math.pi * time / profile.speed) - 1)/(-2)

  r = int(curr_color[0] * curr_strength)
  g = int(curr_color[1] * curr_strength)
  b = int(curr_color[2] * curr_strength)

  return (r, g, b)