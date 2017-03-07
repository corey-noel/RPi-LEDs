#RPi LEDs
Some python scripts to control the LED lights in my living room via a Raspberry Pi.
LED.py interfaces with the GPIO pins, and LED_control.py allows for easier interfacing from the command line.
Uses the pigpio library.

#Usage
##Set a color manually
`python set_color.py #RRGGBB`

##Run a cycle
`python LED_control.py [name of cycle] [profile filename]`
> `[name of cycle]` should be the name of a module in the same directory as LED_control.py.
> That module should contain a function cycle(profile, time) where profile is an instance of the ColorProfile object (as defined in LED_control.py), and time is the current system time, used to control the cycles.
