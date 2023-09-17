import machine
import time
import math

RedLED=machine.Pin(15)
GreenLED=machine.Pin(16)
BlueLED=machine.Pin(17)

RedPWM = machine.PWM(RedLED, freq=1000)
GreenPWM = machine.PWM(GreenLED, freq=1000)
BluePWM = machine.PWM(BlueLED, freq=1000)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)
while True:
    for i in range(100):
        pulse(RedPWM, 100)
        for j in range(50):
            pulse(GreenPWM, 100)
            for K in range(10):
                pulse(BluePWM, 100)
