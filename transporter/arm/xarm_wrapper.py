#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

import time
import traceback
from math import sqrt
from transporter.core.config.config import EndEffectorInstructionObject as DATA, EndEffectorInstructionReg as EIG
from comm.arduino.arduino_udp import ArduinoUdp
from utils.utils import obj_to_json_string as convert

try:
    from xarm.tools import utils
except:
    pass
from xarm import version
from xarm.wrapper import XArmAPI

locals_keys = list(locals().keys())


def pprint(*args, **kwargs):
    try:
        stack_tuple = traceback.extract_stack(limit=2)[0]
        print('[{}][{}]'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), stack_tuple[1]),
              end=' ')
    except:
        pass
    print(*args, **kwargs)


pprint(f'xArm-Python-SDK Version:{version.__version__}')


class SingletonException(Exception):

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass


class XArmWrapperSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if XArmWrapperSingleton.__instance is None:
            XArmWrapperSingleton()
        return XArmWrapperSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if XArmWrapperSingleton.__instance is not None:
            raise SingletonException("This class is a singleton!")
        else:
            self.params = {'speed': 100, 'acc': 2000, 'angle_speed': 20, 'angle_acc': 500, 'events': {},
                           'variables': {},
                           'callback_in_thread': True, 'quit': False}
            XArmWrapperSingleton.__instance = self
            self.arm = XArmAPI('192.168.1.229', do_not_open=True)
            self.end_effector = ArduinoUdp('192.168.1.230')
            self.arm_is_busy = False
            self.arm.connect()
            self.arm.clean_warn()
            self.arm.clean_error()
            self.blower(0)
            self.vacuum_granular(0)
            self.vacuum_solid(0)
            print(self.move_granular(0))
            print(self.move_syringe(0))
            print(self.move_cylinder(0))

            time.sleep(1)
            self.arm.motion_enable(True)
            self.arm.set_mode(0)
            self.arm.set_state(0)
            self.initial_position()
            time.sleep(1)
            self.arm.register_error_warn_changed_callback(self.error_warn_change_callback)
            self.arm.register_state_changed_callback(self.state_changed_callback)
            self.arm.register_report_location_callback(self.location_change_callback)

            if hasattr(self.arm, 'register_count_changed_callback'):
                def count_changed_callback(data):
                    pprint('counter val: {}'.format(data['count']))

                self.arm.register_count_changed_callback(count_changed_callback)
            self.arm.register_connect_changed_callback(self.connect_changed_callback)

    def update_parameters(self, speed=100, acc=2000, angle_speed=20, angle_acc=500):
        self.params['speed'] = speed
        self.params['angle_speed'] = angle_speed
        self.params['acc'] = acc
        self.params['angle_acc'] = angle_acc

    def move_join(self, servo_id=None, angle=None, speed=None, mvacc=None, mvtime=None,
                  relative=False, is_radian=None, wait=False, timeout=None, radius=None, **kwargs):
        code = self.arm.set_servo_angle(angle=angle, speed=self.params['angle_speed'],
                                        mvacc=self.params['angle_acc'], wait=wait, radius=radius)
        if code != 0:
            self.params['quit'] = True
            pprint('set_servo_angle, code={}'.format(code))

    def set_gripper_position(self, pos, wait=True, speed=None, auto_enable=False, timeout=None, is_modbus=True,
                             **kwargs):
        if self.arm.error_code == 0 and not self.params['quit']:
            code = self.arm.set_gripper_position(pos, wait=wait, speed=speed, auto_enable=True)
            if code != 0:
                self.params['quit'] = True
                pprint('set_gripper_position, code={}'.format(code))

    def move_arc_line(self, x=None, y=None, z=None, roll=None, pitch=None, yaw=None, radius=50, wait=False):
        code = self.arm.set_position(*[x, y, z, roll, pitch, yaw], speed=self.params['speed'],
                                     mvacc=self.params['acc'],
                                     radius=radius, wait=wait)
        if code != 0:
            self.params['quit'] = True
            pprint('set_position, code={}'.format(code))

    def initial_position(self):
        self.arm.set_servo_angle(angle=[0.0, -60.0, 0.0, 0.0, 60.0, 0.0], speed=self.params['angle_speed'],
                                 mvacc=self.params['angle_acc'], wait=True, radius=-1.0)

    def is_arm_busy(self):
        return self.arm_is_busy

    def set_is_arm_busy(self, status=False):
        self.arm_is_busy = status

    def set_pause_time(self, pause_time):
        self.arm.set_pause_time(pause_time)

    def is_working_envelope(self, x, y, z):
        radius_xy = sqrt(x ** 2 + y ** 2)
        if 191 < radius_xy > 600:
            return True
        else:
            return False

    # Register error/warn changed callback
    def location_change_callback(self, data):
        c = data['cartesian']
        # print(f'{c[0]} X {c[1]} = {self.is_working_envelope(c[0], c[1], c[2])}')
        if self.is_working_envelope(c[0], c[1], c[2]):
            pass
            # self.arm.emergency_stop()
        # if data and data['error_code'] != 0:
        #     self.arm.set_state(4)
        #     self.params['quit'] = True
        #     pprint('err={}, quit'.format(data['error_code']))
        #     self.arm.release_error_warn_changed_callback(self.error_warn_change_callback)

        # Register error/warn changed callback

    def error_warn_change_callback(self, data):
        if data and data['error_code'] != 0:
            self.arm.set_state(4)
            self.params['quit'] = True
            pprint('err={}, quit'.format(data['error_code']))
            self.arm.release_error_warn_changed_callback(self.error_warn_change_callback)

    # Register state changed callback
    def state_changed_callback(self, data):
        if data and data['state'] == 4:
            if self.arm.version_number[0] >= 1 and self.arm.version_number[1] >= 1 and self.arm.version_number[2] > 0:
                self.params['quit'] = True
                pprint('state=4, quit')
                self.arm.release_state_changed_callback(self.state_changed_callback)

    def connect_changed_callback(self, data):
        if data and not data['connected']:
            self.params['quit'] = True
            pprint('disconnect, connected={}, reported={}, quit'.format(data['connected'], data['reported']))
            self.arm.release_connect_changed_callback(self.error_warn_change_callback)

    def is_connected(self):
        return self.arm.connected

    def move_granular(self, position):
        """
        :param position: maximum value is 9000
        :return:
        """
        if position > EIG.MAX_GRANULAR:
            print(f'invalid position : {position} is more than maximum position')
            position = EIG.MAX_GRANULAR
        ret = self.end_effector.send(convert(DATA(EIG.MOVE_GRANULAR_MOTOR, position)))
        print(ret)
        return ret[0]

    def move_syringe(self, position):
        """
        :param position: maximum value is 13000
        :return:
        """

        if position > EIG.MAX_SYRINGE:
            print(f'invalid position : {position} is more than maximum position')
            position = EIG.MAX_SYRINGE

        ret = self.end_effector.send(convert(DATA(EIG.MOVE_PULLER_MOTOR, position)))
        print(ret)
        return ret[0]

    def move_cylinder(self, position):
        """
        :param position: maximum value is 13000
        :return:
        """
        if position > EIG.MAX_CYLINDER:
            print(f'invalid position : {position} is more than maximum position')
            position = EIG.MAX_CYLINDER
            self.end_effector.send(convert(DATA(EIG.MOVE_CYLINDER_MOTOR, position)))
        ret = self.end_effector.send(convert(DATA(EIG.MOVE_CYLINDER_MOTOR, position)))
        print(ret)
        return ret[0]

    def vacuum_solid(self, position):
        if position == 0:
            ret = self.end_effector.send(convert(DATA(EIG.OFF_CYLINDER_VACUUM, position)))
            print(ret)
            return ret[0]
        else:
            ret = self.end_effector.send(convert(DATA(EIG.ON_CYLINDER_VACUUM, position)))
            print(ret)
            return ret[0]

    def vacuum_granular(self, position):
        if position == 0:
            ret = self.end_effector.send(convert(DATA(EIG.OFF_GRANULAR_VACUUM, position)))
            print(ret)
            return ret[0]
        else:
            ret = self.end_effector.send(convert(DATA(EIG.ON_GRANULAR_VACUUM, position)))
            print(ret)
            return ret[0]

    def blower(self, position):
        if position == 0:
            ret = self.end_effector.send(convert(DATA(EIG.OFF_BLOWER, position)))
            print(ret)
            return ret[0]
        else:
            ret = self.end_effector.send(convert(DATA(EIG.ON_BLOWER, position)))
            print(ret)
            return ret[0]

    def reset(self, speed=None, mvacc=None, mvtime=None, is_radian=None, wait=False, timeout=None):
        self.arm.reset(speed=speed, mvacc=mvacc, mvtime=mvtime, is_radian=is_radian, wait=wait, timeout=timeout)


# bawang 130 - 80 (50)gram = 11000 steps
# brocolli 124 - 80 (44)gram = 11000 steps
# chicken 55(gram) 11000 steps

if __name__ == '__main__':
    from transporter.xarm_scripts.racka import RackA
    from transporter.xarm_scripts.rackb import RackB
    from transporter.xarm_scripts.rackc import RackC
    from transporter.xarm_scripts.rackd import RackD
    from transporter.xarm_scripts.racke import RackE
    from transporter.xarm_scripts.rackf import RackF
    from transporter.xarm_scripts.rackg import RackG
    from transporter.xarm_scripts.rackh import RackH
    from transporter.xarm_scripts.racki import RackI
    from transporter.xarm_scripts.rackj import RackJ
    from transporter.xarm_scripts.rackk import RackK
    from transporter.xarm_scripts.rackl import RackL

    x_arm_motions_directory = {
        1: {1: RackA(), 2: RackB(), 3: RackC(), 4: RackD(), 5: RackE(), 6: RackF()},
        2: {1: RackG(), 2: RackH(), 3: RackI(), 4: RackJ(), 5: RackK(), 6: RackL()},
    }


    def return_to_right_requester():
        print('return to left requester')
        from transporter.xarm_scripts.return_to_right_wok import ReturnToRightWok
        ret = ReturnToRightWok()
        ret.set_type("SOLID")
        ret.run()


    def return_to_left_requester():
        from transporter.xarm_scripts.return_to_left_wok import ReturnToLeftWok
        ret = ReturnToLeftWok()
        ret.set_type("SOLID")
        ret.run()


    motion = x_arm_motions_directory[1][1]
    motion.set_requester(requester_callback=return_to_right_requester)
    motion.set_type("SOLID")
    arm: XArmWrapperSingleton = XArmWrapperSingleton.get_instance()
    while arm.is_arm_busy():
        pass
    motion.run()
