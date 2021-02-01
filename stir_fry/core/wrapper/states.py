#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

import json


class ModuleState:
    RUNNING = 'RUNNING'
    IDLE = 'IDLE'
    ERROR = 'ERROR'

    def __init__(self, module_name: str = None):
        self.module_name = module_name
        self.horizontal_status = self.IDLE
        self.vertical_status = self.IDLE
        self.induction_status = self.IDLE
        self.oil_pump_status = self.IDLE
        self.water_pump_status = self.IDLE
        self.fan_status = self.IDLE
        self.time_lapse = 0
        self.temperature = 36.0
        self.is_plate_ready = False
        self.current_process = ''

    def __str__(self):
        return json.dumps(self.__dict__)


class ModuleStateFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if ModuleStateFactory.__instance is None:
            ModuleStateFactory()
        return ModuleStateFactory.__instance

    def __init__(self):
        if ModuleStateFactory.__instance is not None:
            raise Exception("Module State is singleton")
        else:
            self.__modules_states = []
            ModuleStateFactory.__instance = self

    def register(self, module):
        state = ModuleState(module.name)
        self.__modules_states.append(state)

    def get_state(self, module_name: str):
        for i in self.__modules_states:
            if isinstance(i, ModuleState):
                if i.module_name == module_name:
                    return i

    def update_state(self, module_name: str, horizontal_status=None, vertical_status=None, induction_status=None,
                     oil_pump_status=None, water_pump_status=None, time_lapse=0, temperature=0.0, fan_status=None,
                     current_process=None, is_plate_ready=None):
        for x, i in enumerate(self.__modules_states):
            if isinstance(i, ModuleState):
                if i.module_name == module_name:
                    if temperature != 0.0:
                        self.__modules_states[x].temperature = temperature
                    if horizontal_status is not None:
                        self.__modules_states[x].horizontal_status = horizontal_status
                    if vertical_status is not None:
                        self.__modules_states[x].vertical_status = vertical_status
                    if induction_status is not None:
                        self.__modules_states[x].induction_status = induction_status
                    if oil_pump_status is not None:
                        self.__modules_states[x].oil_pump_status = oil_pump_status
                    if water_pump_status is not None:
                        self.__modules_states[x].water_pump_status = water_pump_status
                    if time_lapse != 0:
                        self.__modules_states[x].time_lapse = time_lapse
                    if fan_status is not None:
                        self.__modules_states[x].fan_status = fan_status
                    if current_process is not None:
                        self.__modules_states[x].current_process = current_process

                    if is_plate_ready is not None:
                        self.__modules_states[x].is_plate_ready = is_plate_ready

                    # print(self.__modules_states[x])
                    return self.__modules_states[x]
