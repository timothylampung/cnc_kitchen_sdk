import time

from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton, SingletonException


class BaseMovement:
    OPEN = 200
    CLOSE = 80

    def __init__(self):
        self.requester_callback = None
        self.x_arm = None
        self.ingredient = None
        try:
            self.x_arm: XArmSDKSingleton = XArmSDKSingleton()
        except SingletonException as e:
            self.x_arm: XArmSDKSingleton = XArmSDKSingleton.get_instance()

    def set_requester(self, requester_callback=None):
        self.requester_callback = requester_callback

    def set_ingredient(self, ingredient):
        self.ingredient = ingredient

    def dispense(self):
        if self.ingredient["type"] == "LIQUID":
            self.x_arm.move_puller(0)
            self.x_arm.move_puller(1000)
            self.x_arm.move_puller(0)
            self.x_arm.move_syringe(0)
        elif self.ingredient["type"] == "SOLID":
            self.x_arm.vacuum_off(0)
            self.x_arm.move_cylinder(0)
            self.x_arm.move_cylinder(5000)
            self.x_arm.move_cylinder(0)
        else:
            print('POWDER')
        self.x_arm.initial_position()

    def suck(self, volume):
        z = self.x_arm.arm.get_position()[1][2]
        self.x_arm.move_arc_line(z=-115.6, wait=True)
        self.x_arm.move_syringe(XArmSDKSingleton.MAX_SYRINGE)
        self.x_arm.move_puller(volume)
        self.x_arm.move_arc_line(z=-36.6, wait=True)

    def vacuum_in(self, ingredient, volume):
        # print()
        x = self.x_arm.arm.get_position()[1][0]
        y = self.x_arm.arm.get_position()[1][1]
        z = self.x_arm.arm.get_position()[1][2]

        self.x_arm.move_cylinder(self.x_arm.MAX_CYLINDER)
        self.x_arm.vacuum_on(0)

        for a in range(2):
            self.x_arm.move_arc_line(z=-118.6, wait=True)
            self.x_arm.move_arc_line(z=z, x=x + 20, wait=True)

            self.x_arm.move_arc_line(z=-118.6, wait=True)
            self.x_arm.move_arc_line(z=z, x=x - 40, wait=True)

            self.x_arm.move_arc_line(z=-118.6, wait=True)
            self.x_arm.move_arc_line(z=z, x=x, wait=True)

        self.x_arm.move_arc_line(z=-36, wait=True)
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
        if isinstance(self.x_arm, XArmSDKSingleton):
            return not self.x_arm.is_arm_busy()

    def get_address(self):
        pass
