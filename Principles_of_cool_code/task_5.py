class Lamp:
    @staticmethod
    def turn_on():
        print('Lamp turned on')

    @staticmethod
    def turn_off():
        print('Lamp turned off')


class MotionSensor:
    @staticmethod
    def turn_on():
        print('Motion sensor turned on')

    @staticmethod
    def turn_off():
        print('Motion sensor turned off')


class Thermostat:
    @staticmethod
    def turn_on():
        print('Thermostat turn on')

    @staticmethod
    def turn_off():
        print('Thermostat turn off')


class SmartHome:
    def __init__(self, list_of_devices):
        self.list_of_devices = list_of_devices

    def turn_on(self):
        for device in self.list_of_devices:
            device.turn_on()

    def turn_off(self):
        for device in self.list_of_devices:
            device.turn_off()
