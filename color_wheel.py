import math

## cycles through a range of colors using offset sine waves
r_offset = 0.0
g_offset = 2.0/3.0 * math.pi
b_offset = 4.0/3.0 * math.pi

def cycle(profile, time):
  r = (int((math.sin((time + r_offset) / profile.speed) + 1) * 128))
  g = (int((math.sin((time + g_offset) / profile.speed) + 1) * 128))
  b = (int((math.sin((time + b_offset) / profile.speed) + 1) * 128))

  return (r, g, b)