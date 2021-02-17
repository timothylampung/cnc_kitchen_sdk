import time

from transporter.arm.xarm_wrapper import XArmWrapperSingleton, SingletonException
from transporter.core.config.config import EndEffectorInstructionReg as EIG


class BaseMovement:
    OPEN = 200
    CLOSE = 80

    def __init__(self):
        self.requester_callback = None
        self.x_arm = None
        self.ingredient = None
        try:
            self.x_arm: XArmWrapperSingleton = XArmWrapperSingleton()
        except SingletonException as e:
            self.x_arm: XArmWrapperSingleton = XArmWrapperSingleton.get_instance()

    def set_requester(self, requester_callback=None):
        self.requester_callback = requester_callback

    def set_type(self, ingredient):
        self.ingredient = ingredient

    def dispense(self):
        if self.ingredient == 'LIQUID':
            self.x_arm.move_syringe(0)
            self.x_arm.move_syringe(5000)
            self.x_arm.move_syringe(0)
        elif self.ingredient == 'SOLID':
            self.x_arm.vacuum_solid(0)
            self.x_arm.blower(1)
            self.x_arm.move_cylinder(0)
            self.x_arm.move_cylinder(5000)
            self.x_arm.move_cylinder(0)
        else:
            self.x_arm.vacuum_granular(0)
            self.x_arm.blower(1)
            self.x_arm.move_granular(0)
            self.x_arm.move_granular(EIG.MAX_GRANULAR)
            self.x_arm.move_granular(0)
            time.sleep(2)
            self.x_arm.blower(0)
            print('POWDER')
        self.x_arm.blower(0)
        self.x_arm.initial_position()

    def suck(self, volume):
        z = self.x_arm.arm.get_position()[1][2]
        # self.x_arm.move_arc_line(z=-115.6, wait=True)
        self.x_arm.move_syringe(EIG.MAX_SYRINGE)
        time.sleep(2)
        # self.x_arm.move_arc_line(z=-36.6, wait=True)

    def vacuum_powder(self, ingredient, volume):
        x = self.x_arm.arm.get_position()[1][0]
        y = self.x_arm.arm.get_position()[1][1]
        z = self.x_arm.arm.get_position()[1][2]
        print(f'Vacuuming solid at position {x}, {y}, {z}')
        self.x_arm.move_granular(EIG.MAX_GRANULAR)
        self.x_arm.vacuum_granular(1)
        for a in range(2):
            self.x_arm.move_arc_line(z=-36, wait=True)
            self.x_arm.move_arc_line(z=z, wait=True)

            self.x_arm.move_arc_line(z=-36, wait=True)
            self.x_arm.move_arc_line(z=z, wait=True)

            self.x_arm.move_arc_line(z=-36, wait=True)
            self.x_arm.move_arc_line(z=z, wait=True)

    def vacuum_in(self, ingredient, volume):

        self.x_arm.move_cylinder(EIG.MAX_CYLINDER)
        self.x_arm.vacuum_solid(1)

        x = self.x_arm.arm.get_position()[1][0]
        y = self.x_arm.arm.get_position()[1][1]
        z = self.x_arm.arm.get_position()[1][2]
        print(f'Vacuuming solid at position {x}, {y}, {z}')

        for a in range(2):
            # self.x_arm.move_arc_line(z=-118.6, wait=True)
            self.x_arm.move_arc_line(z=-36, wait=True)
            self.x_arm.move_arc_line(z=z, wait=True)

            self.x_arm.move_arc_line(z=-36, wait=True)
            self.x_arm.move_arc_line(z=z, wait=True)

            self.x_arm.move_arc_line(z=-36, wait=True)
            self.x_arm.move_arc_line(z=z, wait=True)

            # self.x_arm.move_arc_line(z=z, x=x + 20, wait=True)

            # self.x_arm.move_arc_line(z=-118.6, wait=True)
            # self.x_arm.move_arc_line(z=-36, wait=True)
            # self.x_arm.move_arc_line(z=z, x=x - 40, wait=True)
            #
            # self.x_arm.move_arc_line(z=-118.6, wait=True)
            # self.x_arm.move_arc_line(z=-36, wait=True)
            # self.x_arm.move_arc_line(z=z, x=x, wait=True)

        # self.x_arm.move_arc_line(z=-36, wait=True)
        self.x_arm.move_cylinder(volume)

    def run(self):
        pass
        # if isinstance(self.xArm, XArmSDKSingleton):
        #     if self.xArm.is_connected():
        #         pass
        #     else:
        #         raise Exception('Xarm is not connected!')

    def get_eta(self):
        """in seconds"""
        pass

    def arm_can_move(self):
        if isinstance(self.x_arm, XArmWrapperSingleton):
            return not self.x_arm.is_arm_busy()

    def get_address(self):
        pass
