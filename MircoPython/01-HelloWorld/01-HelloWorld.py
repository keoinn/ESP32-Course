import time
print('MicroPython Ready...')
Count = 0

try:
    while 1:
        Count = Count + 1
        print("Count {}: Hello MircoPython".format(Count))
        time.sleep(1)
except Exception as e:
    print(e)
