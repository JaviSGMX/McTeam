from machine import Pin
import time

pico_led = Pin(25, Pin.OUT)
ir = Pin(15, Pin.OUT)
receiver = Pin(16, Pin.IN)


while True:
    # Se prende el sensor para que siempre
    # este emitiendo luz infraroja
    ir.value(1)
    

    print(receiver.value())
    
    if(receiver.value() == 1):
        pico_led.value(1)
    else:
        pico_led.value(0)
        
    time.sleep(1)
