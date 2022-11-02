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
from time import sleep

SW = Pin(15, Pin.IN, Pin.PULL_UP)
DT = Pin(14, Pin.IN)      # encoder sin módulo Pin(14, Pin.IN, Pin.PULL_UP)
CLK  = Pin(13, Pin.IN)    # encoder sin módulo Pin(13, Pin.IN, Pin.PULL_UP)

valor_anterior = True
switch_presionado = False

while True:
     if valor_anterior != CLK.value():
         if CLK.value() == False:
             if DT.value() == False:
                 print("antihorario")
                 sleep(0.2)
             else:
                 print("horario")
                 sleep(0.2)
         valor_anterior = CLK.value()   
    
     if SW.value() == False and not switch_presionado:
         print("SW presionado") 
         switch_presionado = True
     if SW.value() == True and switch_presionado:
         switch_presionado = False
´´´
