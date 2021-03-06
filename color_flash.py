import math

## cycles through an array of colors
## fades each color out before fading the next one in
def cycle(profile, time):
  curr_color = colors[int(time / profile.speed) % len(colors)]
  curr_strength = (math.cos(2 * math.pi * time / profile.speed) - 1)/(-2)

  r = int(curr_color[0] * curr_strength)
  g = int(curr_color[1] * curr_strength)
  b = int(curr_color[2] * curr_strength)

  return (r, g, b)