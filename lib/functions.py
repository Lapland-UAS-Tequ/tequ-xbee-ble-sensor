import utime


def toI8(byte, scaling):
    return float((byte + 2 ** 7) % 2 ** 8 - 2 ** 7) * scaling


def log(string):
    #dateArray = utime.localtime()
    #ts = "%02d-%02d-%02d %02d:%02d:%02d" % (
    #    dateArray[0], dateArray[1], dateArray[2], dateArray[3], dateArray[4], dateArray[5])

    print("%s : %s" % (utime.ticks_ms(), string))


def getXBeeInternalTemperature(xbeeObj):
    reading = xbeeObj.atcmd('TP')

    if reading > 0x7FFF:
        reading = reading - 0x10000

    return reading


def getXBeeVoltage(xbeeObj):
    reading = xbeeObj.atcmd('%V')
    return reading


def configureXBee3asBLESensor(xbeeObj):
    log("Configuring XBee...")
    xbeeObj.atcmd('BD', 7)
    xbeeObj.atcmd('NB', 0)
    xbeeObj.atcmd('SB', 0)
    xbeeObj.atcmd('SM', 6)

    xbeeObj.atcmd('DO', 4)
    xbeeObj.atcmd('D1', 0)
    xbeeObj.atcmd('D2', 4)
    xbeeObj.atcmd('D3', 4)
    xbeeObj.atcmd('D4', 0) #USER LED
    xbeeObj.atcmd('D5', 4)
    xbeeObj.atcmd('D6', 4)
    xbeeObj.atcmd('D7', 4)
    xbeeObj.atcmd('D8', 4)
    xbeeObj.atcmd('D9', 4)
    xbeeObj.atcmd('P0', 4)
    xbeeObj.atcmd('P1', 4)
    xbeeObj.atcmd('P2', 4)


    xbeeObj.atcmd('P5', 0)
    xbeeObj.atcmd('P6', 0)
    xbeeObj.atcmd('P7', 0)
    xbeeObj.atcmd('P8', 0)
    xbeeObj.atcmd('P9', 0)


def configureSingleParameter(xbeeObj, parameter, value):
    xbeeObj.atcmd(parameter, value)

def setSleepmode(xbeeObj,value):
    xbeeObj.atcmd('SM', value)


def setLED(pin, value):
    pin.value(value)


def Average(lst):
    return sum(lst) / len(lst)


def mapSensorValueToRange(x, a, b, c, d):
    return ((x-a) / (b-a) * (d-c) + c)

def isNaN(num):
    return num != num




