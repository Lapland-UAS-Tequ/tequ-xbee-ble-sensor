from tmp102 import Tmp102, oneshot
from functions import log, getXBeeVoltage, getXBeeInternalTemperature, configureSingleParameter
import machine
import utime


class SensorData:
    def __init__(self, xbee, exp):
        log("SensorData: Initializing SensorData...")
        self.x = xbee
        self.dataDict = {}
        self.exp = exp

    def updateXbeeVoltage(self):
        try:
            xbee_voltage = getXBeeVoltage(self.x)
        except Exception as e:
            xbee_voltage = -99
            self.exp.handleException(e, "Reading XBee Voltage Failed...", True, True, True)
        finally:
            self.dataDict["xbee_voltage"] = xbee_voltage

    def updateXbeeInternalTemperature(self):
        try:
            xbee_temp = getXBeeInternalTemperature(self.x)
        except Exception as e:
            xbee_temp = -99
            self.exp.handleException(e, "SensorData: Reading XBee Voltage Failed...", True, True, True)
        finally:
            self.dataDict["xbee_temp"] = xbee_temp

    def updateTMP102Temperature(self):
        try:
            tmp102_sensor = Tmp102(machine.I2C(1, freq=400000), 0x48, shutdown=True)
            tmp102_sensor.initiate_conversion()
            i = 0
            times = 7
            while not tmp102_sensor.conversion_ready:
                i = i + 1
                if i > times:
                    break
                else:
                    # log("SensorData: Waiting 5 ms... %d/%d" % (i, times))
                    utime.sleep_ms(5)

            tmp102_t = tmp102_sensor.temperature
        except Exception as e:
            tmp102_t = -99
            self.exp.handleException(e, "SensorData: TMP102 I2C sensor not connected or not working...", True, True, True)
        finally:
            configureSingleParameter(self.x, 'D1', 0)
            configureSingleParameter(self.x, 'P1', 0)
            self.dataDict["tmp102_t"] = tmp102_t

    def updateValues(self):
        self.updateXbeeVoltage()
        self.updateXbeeInternalTemperature()
        self.updateTMP102Temperature()
        return self.dataDict

    def getValues(self):
        return self.dataDict

    def getValue(self, value):
        return self.dataDict[value]
