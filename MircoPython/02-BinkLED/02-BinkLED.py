from machine import Pin
import time
builtinLED=Pin(2, Pin.OUT)

try:
    while 1:
        builtinLED.value(1)
        time.sleep(0.5)
        builtinLED.value(0)
        time.sleep(0.5)
except Exception as e:
    print(e)