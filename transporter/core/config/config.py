#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133


class EndEffectorInstructionReg:
    MOVE_CYLINDER_MOTOR = {
        'code': 100,
        'name': 'MOVE_CYLINDER_MOTOR'
    }
    MOVE_PULLER_MOTOR = {
        'code': 101,
        'name': 'MOVE_PULLER_MOTOR'
    }
    MOVE_GRANULAR_MOTOR = {
        'code': 102,
        'name': 'MOVE_GRANULAR_MOTOR'
    }

    ON_CYLINDER_VACUUM = {
        'code': 103,
        'name': 'ON_CYLINDER_VACUUM'
    }
    OFF_CYLINDER_VACUUM = {
        'code': 104,
        'name': 'OFF_CYLINDER_VACUUM'
    }
    ON_GRANULAR_VACUUM = {
        'code': 105,
        'name': 'ON_GRANULAR_VACUUM'
    }
    OFF_GRANULAR_VACUUM = {
        'code': 106,
        'name': 'OFF_GRANULAR_VACUUM'
    }
    ON_BLOWER = {
        'code': 107,
        'name': 'ON_BLOWER'
    }
    OFF_BLOWER = {
        'code': 108,
        'name': 'OFF_BLOWER'
    }

    ArduinoRequestTimeOut = 180


    MAX_GRANULAR = 1650
    MAX_CYLINDER = 9500
    MAX_SYRINGE = 9000


class EndEffectorInstructionObject:

    def __init__(self, function=None, position=0):
        self.function = function['code']
        self.position = position
