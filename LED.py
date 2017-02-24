import pigpio
import time

r_pin = 17
g_pin = 24
b_pin = 22

def start():
	global pi
	pi = pigpio.pi()

def set_color(r, g, b):
	pi.set_PWM_dutycycle(r_pin, r)
	pi.set_PWM_dutycycle(g_pin, g)
	pi.set_PWM_dutycycle(b_pin, b)

def stop():
	pi.stop()

## cycle must return a 3-tuple
## (r, g, b) 0 - 255
def run_cycle(cycle, sleep_time=0.05):
	start()
	start_time = time.time()

	try:
		while True:
			set_color(*cycle())
			time.sleep(sleep_time - ((time.time() - start_time) % sleep_time))
	except KeyboardInterrupt:
		pass

	set_color(0, 0, 0)
	stop()
