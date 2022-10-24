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
