import ujson
from functions import log
from sys import print_exception
from machine import Pin
import utime


class config:
    settings = {}

    def __init__(self):
        log("Initializing configuration file")
        self.loadConfig()
        self.LED_PIN_ID = self.getUserLED_ID()
        self.led_pin = Pin(self.LED_PIN_ID, Pin.OUT, value=0)

    def loadConfig(self):
        try:
            log("Loading config file...")
            file = open('/flash/lib/config.json')
            self.settings = ujson.loads(file.read())
            file.close()
        except Exception as e:
            log("Loading config file... FAILED.. Creating default config..")
            print_exception(e)
            self.createDefaultConfig()
        finally:
            log(self.settings)

    def updateConfig(self):
        try:
            log("Updating config file...")
            file = open('/flash/lib/config.json', mode='w')
            file.write(ujson.dumps(self.settings))
            file.close()
        except Exception as e:
            log("Updating config file... FAILED..")
            print_exception(e)
            self.createDefaultConfig()
        finally:
            log(self.settings)

    def createDefaultConfig(self):
        # original values
        log("Falling back to default config...")
        value = {"SEND_INTERVAL": 10}

        self.settings = value
        file = open('/flash/lib/config.json', mode='w')
        file.write(ujson.dumps(value))
        file.close()

    def updateConfigValue(self, parameter, value):
        log("Parameter %s and value: %s => Updating parameter..." % (parameter, value))
        self.settings[parameter] = value

    def getSleepTime(self):
        return self.settings["sleep_time"]

    def getSendInterval(self):
        return self.settings["send_interval"]

    def getCurrentConfigAsJSON(self):
        return ujson.dumps(self.settings)

    def getWDTimeout(self):
        return self.settings["wd_timeout"]

    def getUserLED_ID(self):
        return self.settings["user_led_id"]

    def getVersion(self):
        return self.settings["version"]

    def blinkLed(self):
        self.led_pin.value(1)
        utime.sleep_ms(5)
        self.led_pin.value(0)