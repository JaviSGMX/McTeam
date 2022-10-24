
import machine
import utime
 
led = machine.Pin(16,machine.Pin.OUT)

while True:
    led.value(1)
