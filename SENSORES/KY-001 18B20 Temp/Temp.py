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
import machine, onewire, ds18x20, time


ds_pin = machine.Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
        time.sleep(5)           

´´´
