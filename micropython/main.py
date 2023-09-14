# Bibliotheken laden
from machine import Pin
from time import sleep

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/digixx/pico-ota-test/main/micropython/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()


# Initialisierung der Onboard-LED
led_onboard = Pin("LED", Pin.OUT)
loopmax = 40
loopcntr =  0

# Wiederholung (Endlos-Schleife)
while True:
    # LED einschalten
    led_onboard.on()
    # halbe Sekunde warten
    sleep(0.1)
    # LED ausschalten
    led_onboard.off()
    # 1 Sekunde warten
    sleep(0.2)
    loopcntr += 1
    
    if loopcntr > loopmax:
        loopcntr = 0
        ota_updater.download_and_install_update_if_available()

