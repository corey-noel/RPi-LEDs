import time
import LED
import math

## cycles through a range of colors using offset sin waves

rotation_speed = 2
red_offset = 0.0
green_offset = 2.0/3.0 * math.pi
blue_offset = 4.0/3.0 * math.pi

def wheel_cycle():
	red = (int((math.sin((time.time() + red_offset) / rotation_speed) + 1) * 128))
	green = (int((math.sin((time.time() + green_offset) / rotation_speed) + 1) * 128))
	blue = (int((math.sin((time.time() + blue_offset) / rotation_speed) + 1) * 128))

	return (red, green, blue)

LED.run_cycle(wheel_cycle)
