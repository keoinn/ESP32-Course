import time, ujson, network,utime
import urequests as requests
from mfrc522 import MFRC522
from machine import Pin, Timer, WDT
import ubinascii
import gc

print("Start")
ssid = 'YOUR SSID'
password = 'YOUR PASSWORD'

request_url = 'https://YOUR.DOMIAN/API/'

led = machine.Pin("LED", machine.Pin.OUT)
count = 0
interval_scan = 0 # 每 X 秒掃描一次
timer = Timer()

def blink(timer):
    led.toggle()

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

def uidToBinaryString(uid):
    mystring = ""
    for i in uid:
        mystring = str(i) + mystring
    return mystring

## WLAN Action ##
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)

    
# Wait for connect or fail
max_wait = 20
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >=3:
        break;
    max_wait -=1
    print(f"count: {max_wait}, {wlan.status()}")
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    print("Network connection failed")
else:
    print("Network Connected!")

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
while True:
    #wdt = WDT(timeout=8388) # 看門狗 x ms 檢查一次
    #wdt.feed()
    count = count + 1
    if wlan.isconnected():
        (stat, tag_type) = reader.request(reader.REQIDL)   # 搜尋 RFID 卡片
        if stat == reader.OK:      # 找到卡片
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card_num = uidToString(uid)
                print(count, card_num)
                # Send Data to BackEnd
                post_data = ujson.dumps({ "b": uidToBinaryString(uid), "h": card_num, "m": mac})
                res = requests.post(request_url, headers = {'content-type': 'application/json'}, data = post_data)
                res.close()
                del stat
                del tag_type
                del uid
                del card_num
                del res
                del post_data
                gc.collect()
                timer.init(freq=2.5, mode=Timer.ONE_SHOT, callback=blink)
        else:
            led.off()
                
    else:
        raise RuntimeError('network connection failed')
        led.off()
    #if interval_scan != 0:
    #    time.sleep(interval_scan)
    
    if count > 255:
        count = 0
    

