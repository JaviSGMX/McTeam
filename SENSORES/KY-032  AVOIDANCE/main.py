# INSTITUTO TECNOLOGICO DE TIJUANA 
# INGENERIA EN SISTEMAS COMPUTACIONALES

## MATERIA: SISTEMAS PROGRAMABLES
## Equipo de trabajo
## ALUMNOS:

### Sesma Rosales Ronald 20211124

### Rolando Arellano Munguía 18210453

### Perez Rojas Jairo Jaziel 18210515

### Esteban Sánchez Garzón Javier 18210527

### Mario ivan jimenez fierro 17212145

###  Claudio Espinoza Murillo 17211519

´´´python

import machine
import utime
reed = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(17, machine.Pin.OUT)
while True:
    if reed.value() == 0:
        led.value(0)
        print("IR Sensor Detected!")
        utime.sleep(0.2)
        led.value(1)
 ´´´
