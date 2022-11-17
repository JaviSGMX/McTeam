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
    
    from machine import Pin
import utime

sensor=Pin(26, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Ningun campo detectado")
        utime.sleep(1)    
    else:
        print("Campo magnetico detectado")
        utime.sleep(1)
utime.sleep(1)
    
    
´´´
