from machine import Pin
import time

button=Pin(1, Pin.IN)
led=Pin(12, Pin.OUT)

while True:
    state=button.value()
    led.value(state)
    time.sleep(0.1)
