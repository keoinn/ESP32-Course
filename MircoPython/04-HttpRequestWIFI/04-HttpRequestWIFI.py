import network
import urequests as requests
import time

ap_ssid = "YOUR SSID"
ap_password = "YOUR PASSWORD"
header = {"Content-Type":"application/json"}


def mac2Str(mac): 
    return ':'.join([f"{b:02X}" for b in mac])

sta_if = network.WLAN(network.STA_IF)
wlan_mac = sta_if.config('mac')
wlan_mac_str = mac2Str(wlan_mac)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(ap_ssid, ap_password)
    while not sta_if.isconnected():
        pass
else:
    print('network config:', sta_if.ifconfig())
    print('Connected ... ')
    while True:
        url = "https://YOUR.DOAMIN/sensor/save?m="+ wlan_mac_str +"&t=Temp&v=23.4"
        response = requests.get(url, headers = header)
        print(url)
        response.close()
        time.sleep(10)


    
