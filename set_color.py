from sys import argv
import LED

LED.start()

if len(argv) < 4:
	LED.set_color(0, 0, 0)

else:
	LED.set_color(int(argv[1], 16), int(argv[2], 16), int(argv[3], 16))

LED.stop()
