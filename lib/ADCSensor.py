from functions import log
from functions import mapSensorValueToRange
from functions import Average

from machine import ADC
import time

class ADCSensor:

    def __init__(self, xbee, ADC_PIN_ID, input_range_min, input_range_max, target_range_min, target_range_max):
        log("ADC Sensor is connected to PIN %s" % ADC_PIN_ID)
        self.ADC_PIN = ADC(ADC_PIN_ID)
        self.a = input_range_min
        self.b = input_range_max
        self.c = target_range_min
        self.d = target_range_max
        self.x = xbee
        self.adc_ref = 0.0
        log("Configuring ADC reference voltage...")
        self.configureADCReference()

    def getADCSensorValue(self, samples, timeBetweenSamples, HighSamplesToRemove, LowSamplesToRemove, offset):
        if samples < 0:
            samples = 1

        samples_array = []

        for x in range(samples):
            adc_value = self.ADC_PIN.read() - offset
            samples_array.append(adc_value)
            time.sleep(timeBetweenSamples)

        for x in range(HighSamplesToRemove):
            samples_array.remove(max(samples_array))

        for x in range(LowSamplesToRemove):
            samples_array.remove(min(samples_array))

        log(samples_array)

        min_value = min(samples_array)
        max_value = max(samples_array)
        avg_value = Average(samples_array)
        vpp_value = (avg_value * self.adc_ref / 4095)
        vrms_value = vpp_value / 2 * 0.707

        log("min: %.0f, max: %.0f, avg: %.6f, Vpp: %.6f, Vrms: %.6f"
            % (min_value, max_value, avg_value, vpp_value, vrms_value))

        #adc_voltage = (adc_value * self.adc_ref / 4095)
        #sensor_value = mapSensorValueToRange(adc_voltage, self.a, self.b, self.c, self.d)
        return [min_value, max_value, avg_value, vpp_value, vrms_value]

    def configureADCReference(self):
        # ADC reference voltage
        AV_VALUES = {0: 1.25, 1: 2.5, 2: 3.3, None: 2.5}

        # Read the module's Analog Digital Reference
        try:
            av = self.x.atcmd("AV")
        except KeyError:
            # Reference is set to 2.5 V on XBee 3 Cellular
            av = None
        reference = AV_VALUES[av]
        log("Configured Analog Digital Reference: AV:{}, {} V".format(av, reference))
        self.adc_ref = reference
