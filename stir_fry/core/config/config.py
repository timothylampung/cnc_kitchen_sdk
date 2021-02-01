#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

class ArduinoConf(object):

    def __init__(self):
        pass

    class InstructionReg:
        ROTATE_HORIZONTAL_MOTOR = {
            'code': 50,
            'name': 'ROTATE_HORIZONTAL_MOTOR'
        }
        STOP_HORIZONTAL_MOTOR = {
            'code': 51,
            'name': 'STOP_HORIZONTAL_MOTOR'
        }
        SHAKE_HORIZONTAL = {
            'code': 52,
            'name': 'SHAKE_HORIZONTAL'
        }
        ZERO_VERTICAL = {
            'code': 53,
            'name': 'ZERO_VERTICAL'
        }
        FLIP_VERTICAL = {
            'code': 54,
            'name': 'FLIP_VERTICAL'
        }
        PLATE_VERTICAL = {
            'code': 55,
            'name': 'PLATE_VERTICAL'
        }
        VERTICAL_HOLD_45 = {
            'code': 56,
            'name': 'VERTICAL_HOLD_45'
        }
        VERTICAL_FOR_PICKING = {
            'code': 57,
            'name': 'VERTICAL_FOR_PICKING'
        }
        PORTION = {
            'code': 101,
            'name': 'PORTION'
        }
        GET_TEMPERATURE = {
            'code': 10,
            'name': 'GET_TEMPERATURE'
        }
        GET_LIMIT_SW_HORIZONTAL = {
            'code': 11,
            'name': 'GET_LIMIT_SW_HORIZONTAL'
        }
        GET_PROXIMITY = {
            'code': 12,
            'name': 'GET_PROXIMITY'
        }
        GET_LOAD_CELL = {
            'code': 13,
            'name': 'GET_LOAD_CELL'
        }
        OPEN_WATER_VALVE = {
            'code': 30,
            'name': 'OPEN_WATER_VALVE'
        }
        CLOSE_WATER_VALVE = {
            'code': 31,
            'name': 'CLOSE_WATER_VALVE'
        }
        CLOSE_OIL_VALVE = {
            'code': 32,
            'name': 'CLOSE_OIL_VALVE'
        }
        ON_INDUCTION_HEATER = {
            'code': 33,
            'name': 'ON_INDUCTION_HEATER'
        }
        OFF_INDUCTION_HEATER = {
            'code': 34,
            'name': 'OFF_INDUCTION_HEATER'
        }
        START_COOLING_FAN = {
            'code': 35,
            'name': 'START_COOLING_FAN'
        }
        STOP_COOLING_FAN = {
            'code': 36,
            'name': 'STOP_COOLING_FAN'
        }
        OPEN_OIL_VALVE = {
            'code': 37,
            'name': 'OPEN_OIL_VALVE'
        }
        RESET = {
            'code': 900,
            'name': 'RESET'
        }
        ArduinoRequestTimeOut = 180

    class InstructionObject:

        def __init__(self, function=None):
            self.function = function['code']

    class UdpSetUp:
        GET_PORT = 8888
        GET_UDP_TIMEOUT = 180
