Ball Switch


from machine import Pin
import utime

pin=27
sensor=Pin(pin, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Sensor detectado")
        utime.sleep(2)    
    else:
        print("No detectado")
        utime.sleep(2)
utime.sleep(1)

![image](Ku-020%20Ball%20Swiy.gif)
