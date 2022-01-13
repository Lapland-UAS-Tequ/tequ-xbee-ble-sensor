# tequ-xbee-ble-sensor

Low power XBee temperature sensor. Broadcasts data via Bluetooth low energy approximately every 30 seconds. Between wakeups device is in deepsleep and consumes ~5-10 uA when using 3.6 VDC battery.

Project has been developed and tested with: 

Digi XBee 3 Zigbee 3 RF Module, model XB3-24Z8UM-J

https://www.digi.com/products/models/xb3-24z8um-j


## Development 

1. Install XCTU

https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu

2. Install Pycharm

https://www.jetbrains.com/pycharm/

3. Install XBee Pycharm plugin

https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/digi-xbee-pycharm-ide-plug-in

4. Clone repository

```
git clone https://github.com/Lapland-UAS-Tequ/tequ-xbee-ble-sensor
```

5. Open cloned folder as Digi project in Pycharm


## Configuration file

/lib/config.json

```
{
  "sleep_time": 30000,
  "wd_timeout": 30000,
  "user_led_id": "D9",
  "version": "Tequ - BLE Sensor [2021-10-27]"
}
```

sleep_time = time between wake ups 
wd_timeout = time after watchdog resets, if it has not been kicked
user_led_id = ID of LED that blinks when app is running

## Receiving data

TBD






