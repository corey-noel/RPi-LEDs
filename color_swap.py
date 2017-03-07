import math

## cycles through an array of colors
## swaps through colors sharply
def cycle(profile, time):
  curr_color = profile.colors[int(time / profile.speed) % len(profile.colors)]

  return (curr_color[0], curr_color[1], curr_color[2])