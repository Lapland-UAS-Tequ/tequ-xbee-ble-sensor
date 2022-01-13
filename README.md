# tequ-xbee-ble-sensor

Low power XBee temperature sensor. Broadcasts data via Bluetooth low energy approximately every 30 seconds. 

Settings can be configured in config.json file.

## Development 

Install XCTU

https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/xctu

Install Pycharm

https://www.jetbrains.com/pycharm/

Install XBee Pycharm plugin

https://www.digi.com/products/embedded-systems/digi-xbee/digi-xbee-tools/digi-xbee-pycharm-ide-plug-in


## Settings file

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






