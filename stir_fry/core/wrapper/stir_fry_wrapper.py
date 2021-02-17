#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133
from comm.arduino.arduino_udp import ArduinoUdp
from stir_fry.core.config.config import ArduinoConf as Ac
from stir_fry.core.config.codes import ArduinoResponseCode as ARC
from utils.utils import obj_to_json_string
from stir_fry.core.wrapper.states import ModuleStateFactory, ModuleState


class StirFryWrapper:

    def __init__(self, ip, module_name):
        self._has_error = False
        self._has_warn = False
        self._state_is_ready = False
        self._error_code = 0
        self._warn_code = 0
        self._cmd_num = 0
        self._debug = False
        self._current_state = None
        self._ip = ip
        self.comm = ArduinoUdp(self._ip)
        self.module_name = module_name
        self.state_factory: ModuleStateFactory = ModuleStateFactory.get_instance()

    def get_temperature(self):
        self._current_state = Ac.InstructionReg.GET_TEMPERATURE['name']
        temp = self.comm.send(self.__convert(Ac.InstructionReg.GET_TEMPERATURE))
        t = 400
        try:
            t = temp[0]["average_temps"]

            """update the states factory"""
            self.state_factory.update_state(
                module_name=self.module_name,
                temperature=t,
            )
            return t
        except Exception as e:
            print(f'Error occur while getting temperatures {e}')
            return t

    def set_vertical_0(self):
        self._current_state = Ac.InstructionReg.ZERO_VERTICAL['name']

        """update the states factory"""
        self.state_factory.update_state(
            module_name=self.module_name,
            vertical_status=ModuleState.RUNNING
        )
        ret = self.comm.send(self.__convert(Ac.InstructionReg.ZERO_VERTICAL))
        if ret[0]['function'] != ARC.PING_VERTICAL_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""
        self.state_factory.update_state(
            module_name=self.module_name,
            vertical_status=ModuleState.IDLE)
        return ret

    def set_vertical_45(self):

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            vertical_status=ModuleState.RUNNING)

        self._current_state = Ac.InstructionReg.VERTICAL_HOLD_45['name']

        ret = self.comm.send(self.__convert(Ac.InstructionReg.VERTICAL_HOLD_45))
        if ret[0]['function'] != ARC.PING_VERTICAL_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            vertical_status=ModuleState.IDLE)
        return ret

    def set_vertical_plating(self):
        self._current_state = Ac.InstructionReg.PLATE_VERTICAL['name']

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            vertical_status=ModuleState.RUNNING)
        ret = self.comm.send(self.__convert(Ac.InstructionReg.PLATE_VERTICAL))

        if ret[0]['function'] != ARC.PING_VERTICAL_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            vertical_status=ModuleState.IDLE)
        return ret

    def rotate_horizontal(self):

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            horizontal_status=ModuleState.RUNNING)

        self._current_state = Ac.InstructionReg.ROTATE_HORIZONTAL_MOTOR['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.ROTATE_HORIZONTAL_MOTOR))

        if ret[0]['function'] != ARC.PING_HORIZONTAL_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        return ret

    def shake_horizontal(self):

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            horizontal_status=ModuleState.RUNNING)

        self._current_state = Ac.InstructionReg.SHAKE_HORIZONTAL['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.SHAKE_HORIZONTAL))

        if ret[0]['function'] != ARC.PING_HORIZONTAL_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        return ret

    def stop_horizontal(self):
        self._current_state = Ac.InstructionReg.STOP_HORIZONTAL_MOTOR['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.STOP_HORIZONTAL_MOTOR))

        if ret[0]['function'] != ARC.PING_HORIZONTAL_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            horizontal_status=ModuleState.IDLE)
        return ret

    def open_oil_valve(self):
        self._current_state = Ac.InstructionReg.OPEN_OIL_VALVE['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.OPEN_OIL_VALVE))
        if ret[0]['function'] != ARC.OPEN_OIL_VALVE_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            oil_pump_status=ModuleState.RUNNING)
        return ret

    def close_oil_valve(self):
        self._current_state = Ac.InstructionReg.OPEN_OIL_VALVE['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.CLOSE_OIL_VALVE))

        if ret[0]['function'] != ARC.CLOSE_OIL_VALVE_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            oil_pump_status=ModuleState.IDLE)
        return ret

    def open_water_valve(self):
        self._current_state = Ac.InstructionReg.OPEN_WATER_VALVE['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.OPEN_WATER_VALVE))

        if ret[0]['function'] != ARC.OPEN_WATER_VALVE_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            water_pump_status=ModuleState.RUNNING)
        return ret

    def close_water_valve(self):
        self._current_state = Ac.InstructionReg.OPEN_WATER_VALVE['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.CLOSE_WATER_VALVE))

        if ret[0]['function'] != ARC.CLOSE_WATER_VALVE_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            water_pump_status=ModuleState.IDLE)
        return ret

    def start_cooling_fan(self):
        self._current_state = Ac.InstructionReg.START_COOLING_FAN['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.START_COOLING_FAN))

        if ret[0]['function'] != ARC.START_COOLING_FAN_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            fan_status=ModuleState.RUNNING)
        return ret

    def stop_cooling_fan(self):
        self._current_state = Ac.InstructionReg.STOP_COOLING_FAN['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.STOP_COOLING_FAN))

        if ret[0]['function'] != ARC.STOP_COOLING_FAN_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            fan_status=ModuleState.IDLE)
        return ret

    def on_induction(self):
        self._current_state = Ac.InstructionReg.ON_INDUCTION_HEATER['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.ON_INDUCTION_HEATER))

        if ret[0]['function'] != ARC.START_INDUCTION_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            induction_status=ModuleState.RUNNING)
        return ret

    def off_induction(self):
        self._current_state = Ac.InstructionReg.OFF_INDUCTION_HEATER['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.OFF_INDUCTION_HEATER))

        if ret[0]['function'] != ARC.STOP_INDUCTION_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        """update the states factory"""""
        self.state_factory.update_state(
            module_name=self.module_name,
            induction_status=ModuleState.IDLE)
        return ret

    def is_plate_present(self):
        self._current_state = Ac.InstructionReg.GET_PROXIMITY['name']
        ret = self.comm.send(self.__convert(Ac.InstructionReg.GET_PROXIMITY))

        if ret[0]['function'] != ARC.GET_PROXIMITY_SUCCESS:
            self._has_error = True
            raise RuntimeError()

        return ret[0]['analog_status'] > 900

    @property
    def state_is_ready(self):
        return self._state_is_ready

    def set_debug(self, debug):
        self._debug = debug

    @staticmethod
    def __convert(instruction):
        return obj_to_json_string(Ac.InstructionObject(instruction))

    def clean_error(self):
        self._has_error = False
        print('error had cleaned')


if __name__ == '__main__':
    wrapper = StirFryWrapper('192.168.1.168', module_name='MODULE_1')
    print(wrapper.off_induction())
    print(wrapper.off_induction())
    print(wrapper.off_induction())
