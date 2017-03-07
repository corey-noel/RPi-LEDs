import math

fade_factor = 8.0

## cycles through an array of colors
## holds colors for a period
## then briefly crossfades
def cycle(profile, time):
  curr_color = profile.colors[int(time / profile.speed) % len(profile.colors)]
  next_color = profile.colors[(int(time / profile.speed) + 1) % len(profile.colors)]

  ratio = (time % profile.speed) / profile.speed

  if ratio < (1 / fade_factor):
    ratio *= fade_factor
  else:
    ratio = 1

  r = int(curr_color[0] * (1 - ratio) + next_color[0] * ratio)
  g = int(curr_color[1] * (1 - ratio) + next_color[1] * ratio)
  b = int(curr_color[2] * (1 - ratio) + next_color[2] * ratio)

  return (r, g, b)