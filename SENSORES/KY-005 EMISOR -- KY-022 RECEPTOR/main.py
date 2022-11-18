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
import time

pico_led = Pin(25, Pin.OUT)
ir = Pin(15, Pin.OUT)
receiver = Pin(16, Pin.IN)


while True:
    ir.value(1)
    
    #Cuando el sensor recibe un valor se prende el led de la Pico
    if(receiver.value() == 1):
        pico_led.value(1)
    else:
        pico_led.value(0)
        
    time.sleep(1)
  
  
  
  
      ´´´
