import math
import LED_control

## cycles through random colors
## crossfades between colors continually
def cycle(profile, time):
  curr_color = LED_control.random_color(int(time / profile.speed))
  next_color = LED_control.random_color(int(time / profile.speed) + 1)
  ratio = (time % profile.speed) / profile.speed

  r = int(curr_color[0] * (1 - ratio) + next_color[0] * ratio)
  g = int(curr_color[1] * (1 - ratio) + next_color[1] * ratio)
  b = int(curr_color[2] * (1 - ratio) + next_color[2] * ratio)

  return (r, g, b)
