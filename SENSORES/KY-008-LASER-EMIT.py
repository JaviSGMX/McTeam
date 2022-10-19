```python
from machine import Pin
import utime

Laser = Pin(18,Pin.OUT)

while True:
    
    Laser.value(1)
    utime.sleep(0.5)
    Laser.value(0)
    utime.sleep(0.5)
```
