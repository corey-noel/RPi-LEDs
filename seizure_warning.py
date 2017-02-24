import LED
import random

def seizure_cycle():
	red = random.randint(0, 255)
	green = random.randint(0, 255)
	blue = random.randint(0, 255)

	return (red, green, blue)


LED.run_cycle(seizure_cycle, .2)
