from mfrc522 import MFRC522
from machine import Pin
import utime

green_led = Pin(22, Pin.OUT) 
red_led  = Pin(26, Pin.OUT)

# 將卡號由 2 進位轉換為 16 進位的字串
def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
              
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
print("..... 請將卡片靠近感應器.....")

try:
    while True:
        (stat, tag_type) = reader.request(reader.REQIDL)   # 搜尋 RFID 卡片
        if stat == reader.OK:      # 找到卡片
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card_num = uidToString(uid)
                print(".....卡片號碼： %s" % card_num)
                if  card_num == '1C49D001':
                    green_led.value(1)   # 讀到授權的卡號後點亮綠色 LED
                    utime.sleep(0.5)       # 亮 2 秒鐘
                    green_led.value(0) 
                else:
                    print(".....卡片錯誤.....")
                    red_led.value(1)    # 讀到非授權的卡號後點亮紅色 LED
                    utime.sleep(0.5)      # 亮 2 秒鐘
                    red_led.value(0)
            else:
                print(".....授權錯誤.....")

except KeyboardInterrupt:
    print(".....Bye.....")