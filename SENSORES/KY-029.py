from machine import Pin
import time

led_pins = [16,17] # pins where RGB LED is wired
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)] # pin control array
delay_t = 0.1 # seconds to delay between toggles
while True: # loop infinitely
    for led in leds: # loop through each led
        led.high() # led high
        time.sleep(delay_t) # wait
        led.low() # led low
        time.sleep(delay_t) # wait
