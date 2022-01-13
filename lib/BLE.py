import utime
from functions import log
from digi import ble
from struct import pack


def form_mac_address(addr: bytes) -> str:
    return ":".join('{:02x}'.format(b) for b in addr)


def form_adv_name(name):
    payload = bytearray()
    payload.append(len(name) + 1)
    payload.append(0x08)
    payload.extend(name.encode())
    return payload


def form_adv_data_dp1(data):
    custom_data = pack("f", data['xbee_voltage'])+pack("f", data['xbee_temp'])+pack("f", data['tmp102_t'])
    payload = bytearray()
    payload.append(len(custom_data) + 4)   # datapacket length
    payload.append(0xFF)            # 0xFF
    payload.append(0x02)            # Manufacturer specific, Digi International Inc (R) = 0x02DB
    payload.append(0xDB)            # Manufacturer specific
    payload.append(0x01)            # Datapacket ID
    payload.extend(custom_data)     # CUSTOM DATA
    return payload


class BLEAdvertise:
    def __init__(self):
        log("Configuring BLE...")

    @staticmethod
    def advertise(advertise_interval_us, data, datapacket_id):
        ble.active(True)
        # log("Started Bluetooth with address of: {}".format(form_mac_address(ble.config("mac"))))
        if datapacket_id == 1:
            payload = form_adv_data_dp1(data)

        log("Advertising payload: {}".format(payload))
        ble.gap_advertise(advertise_interval_us, payload)

    @staticmethod
    def stopAdvertise():
        ble.gap_advertise(None)
        ble.active(False)

    def advertiseOnce(self, advertise_interval_us, data, datapacket_id):
        self.advertise(advertise_interval_us, data, datapacket_id)
        utime.sleep_ms(5)
        self.stopAdvertise()
