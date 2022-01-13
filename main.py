# Import libraries
from functions import log, configureXBee3asBLESensor, configureSingleParameter
import machine
import config
import xbee
import utime
import handleException
import BLE
import data

bootCount = 1
config = config.config()
watchdog = machine.WDT(timeout=config.getWDTimeout(), response=machine.HARD_RESET)
x = xbee.XBee()
exp = handleException.HandleException()
sleep_time = config.getSleepTime()
bt = BLE.BLEAdvertise()
data = data.SensorData(x, exp)
configureXBee3asBLESensor(x)
log(config.getVersion())

# Main program loop, this is repeated while program is running
while 1:
    start = utime.ticks_ms()
    try:
        bt.advertiseOnce(20000, data.updateValues(), 1)
        log("BOOT #: %d | XBEE: %.1f C | VOLTAGE: %.1f | TMP102: %.2f | "
            % (bootCount, data.getValue('xbee_temp'), data.getValue('xbee_voltage'), data.getValue('tmp102_t')))
    except Exception as e:
        exp.handleException(e, "Error in main loop...", True, True, True)
    else:
        if exp.getExceptionCount() < 30:
            log("Feeding watchdog | Exception count: %d " % exp.getExceptionCount())
            watchdog.feed()
        else:
            log("Exception count: %d => Do not feed WatchDog" % exp.getExceptionCount())

        delta = utime.ticks_diff(utime.ticks_ms(), start)
        log("Executing main program took %.3f seconds. Sleeping %d seconds...\n\n" % (delta / 1000, sleep_time))

    finally:
        config.blinkLed()
        bootCount = bootCount + 1
        sleep_ms = x.sleep_now(sleep_time)
