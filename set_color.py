from sys import argv
import LED

## allows direct setting of colors from the command line
LED.start()

if len(argv) == 2:
  if len(argv[1]) != 6:
    print("Error: Invalid input (use a hex code RRGGBB)")
  else:
    LED.set_color(int(argv[1][0:2], 16), int(argv[1][2:4], 16), int(argv[1][4:6], 16))

elif len(argv) == 4:
  LED.set_color(int(argv[1]), int(argv[2]), int(argv[3]))

else:
  LED.set_color(0, 0, 0)

LED.stop()
