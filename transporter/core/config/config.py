#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

class EndEffectorInstructionReg:
    MOVE_PULLER = {
        'code': 1,
        'name': 'MOVE_PULLER'
    }
    MOVE_SYRINGE = {
        'code': 2,
        'name': 'MOVE_CYRINGE'
    }
    MOVE_CYLINDER = {
        'code': 3,
        'name': 'MOVE_CYLINDER'
    }
    VACUUM_GRANULAR_ON = {
        'code': 4,
        'name': 'VACUUM_GRANULAR_ON'
    }
    VACUUM_GRANULAR_OFF = {
        'code': 5,
        'name': 'VACUUM_GRANULAR_ON'
    }
    VACUUM_SOLID_ON = {
        'code': 6,
        'name': 'VACUUM_SOLID_ON'
    }
    VACUUM_SOLID_OFF = {
        'code': 7,
        'name': 'VACUUM_SOLID_OFF'
    }
    BLOWER_GRANULAR_ON = {
        'code': 8,
        'name': 'BLOWER_GRANULAR_ON'
    }
    BLOWER_GRANULAR_OFF = {
        'code': 9,
        'name': 'BLOWER_GRANULAR_OFF'
    }

    ArduinoRequestTimeOut = 180


class EndEffectorInstructionObject:

    def __init__(self, function=None, position=0):
        self.function = function['code']
        self.position = position
