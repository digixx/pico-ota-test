# Bibliotheken laden
from machine import Pin
from time import sleep
from machine import WDT

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/digixx/pico-ota-test/main/micropython/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

# Initialisierung der Onboard-LED
led_onboard = Pin("LED", Pin.OUT)
loopmax = 30
loopcntr =  0

wdt = WDT(timeout=5000)  # enable it with a timeout of 2s

# Wiederholung (Endlos-Schleife)
while True:
    wdt.feed()
    # LED einschalten
    led_onboard.on()
    # halbe Sekunde warten
    sleep(0.1)
    # LED ausschalten
    led_onboard.off()
    # 1 Sekunde warten
    sleep(0.1)
    loopcntr += 1

    if loopcntr > loopmax:
        loopcntr = 0
        ota_updater.download_and_install_update_if_available()

