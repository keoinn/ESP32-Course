#include "WiFi.h"
// WiFi.encryptionType的byte對應表如下
// encryptionType 0:WIFI_AUTH_OPEN
// encryptionType 1:WIFI_AUTH_WEP
// encryptionType 2:WIFI_AUTH_WPA_PSK
// encryptionType 3:WIFI_AUTH_WPA2_PSK
// encryptionType 4:WIFI_AUTH_WPA_WPA2_PSK
// encryptionType 5:WIFI_AUTH_WPA2_ENTERPRISE
// encryptionType 6:WIFI_AUTH_MAX
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

}

void loop() {
   scanAP();
   delay(10000);
}
 
void scanAP(void) {
  int n = WiFi.scanNetworks();
  delay(1000);
  Serial.println("scan Wi-Fi done");
  if (n == 0)
    Serial.println("no Wi-Fi networks found");
  else
  {
    Serial.print(n);
    Serial.println(" Wi-Fi networks found");
    for (int i = 0; i < n; ++i)
     {
      //印出SSID
      Serial.print(i + 1);
      Serial.print(": SSID = ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      // Mac Address
      Serial.print(WiFi.macAddress());
      Serial.print(")");
      //印出RSSI強度
      Serial.print(" (RSSI = ");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      //印出加密模式
      Serial.print(" Encryption Method = ");
      Serial.println(WiFi.encryptionType(i),HEX);
      delay(10);
     }
  }
}
