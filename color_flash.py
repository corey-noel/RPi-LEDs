import math
import LED
import time

## cycles through an array of colors
## fades each color out before fading the next one in
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
speed = 5

def flash_cycle():
	curr_color = colors[int(time.time() / speed) % len(colors)]
	curr_strength = (math.cos(2 * math.pi * time.time() / speed) - 1)/(-2)

	red = int(curr_color[0] * curr_strength)
	green = int(curr_color[1] * curr_strength)
	blue = int(curr_color[2] * curr_strength)

	return (red, green, blue)

LED.run_cycle(flash_cycle)
