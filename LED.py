import pigpio

r_pin = 17
g_pin = 24
b_pin = 22

## must be called before calling set_color
def start():
  global pi
  pi = pigpio.pi()

## sets the color of the LED to r, g, b
def set_color(r, g, b):
  pi.set_PWM_dutycycle(r_pin, r)
  pi.set_PWM_dutycycle(g_pin, g)
  pi.set_PWM_dutycycle(b_pin, b)

## must be called before exiting the program
def stop():
  pi.stop()