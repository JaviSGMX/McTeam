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

```python

from machine import Pin
import utime

sensor = Pin(18, Pin.IN)
utime.sleep(2)

while True:
# Se imprime un mensaje en función del valor del sensor
    if sensor.value() == 1:
        print("No detectada")
    else:
        print("Línea detectada")
    utime.sleep(0.5)

    ´´´
