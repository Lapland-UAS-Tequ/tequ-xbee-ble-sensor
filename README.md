# tequ-xbee-ble-sensor

Low power XBee temperature sensor. Broadcasts data via Bluetooth low energy approximately every 30 seconds. Between wakeups device is in deepsleep and consumes ~5-10 uA when using 3.6 VDC battery.

Project has been developed and tested with Digi XBee 3 Zigbee 3 RF Module, model XB3-24Z8UM-J

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

sleep_time = time in milliseconds between wake ups 

wd_timeout = time in milliseconds after watchdog resets the device, if it has not been kicked

user_led_id = ID of LED that blinks when app is running


## Receiving data in Node-RED 

Tested with Raspberry PI4, draws temperature data to chart. Chart can be viewed with browser http://<RPI4_IP>:1880/ui

```
sudo apt-get install libbluetooth-dev libudev-dev pi-bluetooth
```

```
npm install @abandonware/noble
```
```
npm install node-red-contrib-blebeacon-scanner
```
```
npm install node-red-contrib-buffer-parser
```
```
npm install node-red-contrib-blebeacon-scanner
```
```
npm install node-red-dashboard
```

You might have to run following commmand to make BLE work:

```
sudo setcap cap_net_raw+eip $(eval readlink -f `which node`)
```

https://github.com/noble/noble#running-on-linux


**Example flow:**

```
[{"id":"84b3d433ec997c61","type":"BLE Beacon Scanner","z":"96e1bc43.e1f5","name":"","x":140,"y":720,"wires":[["644f1c3b3f4a073a","af8c13109958567b"]]},{"id":"644f1c3b3f4a073a","type":"debug","z":"96e1bc43.e1f5","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":330,"y":680,"wires":[]},{"id":"af8c13109958567b","type":"switch","z":"96e1bc43.e1f5","name":"Select BLE Sensor ","property":"payload.id","propertyType":"msg","rules":[{"t":"eq","v":"90fd9f06f313","vt":"str"}],"checkall":"true","repair":false,"outputs":1,"x":370,"y":720,"wires":[["3cfcdf4ec0a72b75","d59a682f81b52edf"]]},{"id":"3cfcdf4ec0a72b75","type":"debug","z":"96e1bc43.e1f5","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":550,"y":680,"wires":[]},{"id":"d59a682f81b52edf","type":"buffer-parser","z":"96e1bc43.e1f5","name":"Parse data","data":"payload.other","dataType":"msg","specification":"spec","specificationType":"ui","items":[{"type":"uint16le","name":"manufacturer","offset":0,"length":1,"offsetbit":0,"scale":"1","mask":""},{"type":"uint8","name":"datapacket_id","offset":2,"length":1,"offsetbit":0,"scale":"1","mask":""},{"type":"floatle","name":"supply_voltage","offset":3,"length":1,"offsetbit":0,"scale":"0.001","mask":""},{"type":"floatle","name":"xbee_temperature","offset":7,"length":1,"offsetbit":0,"scale":"1","mask":""},{"type":"floatle","name":"tmp102_temperature","offset":11,"length":1,"offsetbit":0,"scale":"1","mask":""}],"swap1":"","swap2":"","swap3":"","swap1Type":"swap","swap2Type":"swap","swap3Type":"swap","msgProperty":"payload","msgPropertyType":"str","resultType":"keyvalue","resultTypeType":"output","multipleResult":false,"fanOutMultipleResult":false,"setTopic":true,"outputs":1,"x":570,"y":720,"wires":[["c725594b54d3d8bd","a7a3eec37c3fda79"]]},{"id":"c725594b54d3d8bd","type":"debug","z":"96e1bc43.e1f5","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":730,"y":680,"wires":[]},{"id":"0e76b03f79565bb3","type":"ui_chart","z":"96e1bc43.e1f5","name":"","group":"55d19116fd1f7336","order":0,"width":0,"height":0,"label":"chart","chartType":"line","legend":"false","xformat":"HH:mm:ss","interpolate":"linear","nodata":"","dot":false,"ymin":"","ymax":"","removeOlder":1,"removeOlderPoints":"","removeOlderUnit":"3600","cutout":0,"useOneColor":false,"useUTC":false,"colors":["#1f77b4","#aec7e8","#ff7f0e","#2ca02c","#98df8a","#d62728","#ff9896","#9467bd","#c5b0d5"],"outputs":1,"useDifferentColor":false,"x":970,"y":720,"wires":[[]]},{"id":"a7a3eec37c3fda79","type":"change","z":"96e1bc43.e1f5","name":"Set payload for chart","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.tmp102_temperature","tot":"msg"},{"t":"set","p":"topic","pt":"msg","to":"TMP102","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":780,"y":720,"wires":[["0e76b03f79565bb3","21cbe7e2b5bebff1"]]},{"id":"21cbe7e2b5bebff1","type":"debug","z":"96e1bc43.e1f5","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":970,"y":680,"wires":[]},{"id":"55d19116fd1f7336","type":"ui_group","name":"Default","tab":"73e8765f0fa0da8e","order":1,"disp":true,"width":"18","collapse":false},{"id":"73e8765f0fa0da8e","type":"ui_tab","name":"Home","icon":"dashboard","disabled":false,"hidden":false}]
```
