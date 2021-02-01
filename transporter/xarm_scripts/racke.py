from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackE(BaseMovement):

    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            super().run()
            if isinstance(self.x_arm, XArmSDKSingleton):
                self.x_arm.set_is_arm_busy(True)
                self.x_arm.initial_position()
                self.x_arm.move_join(angle=[152.5, 27.1, -73.7, 0.5, 47.2, 28.7], radius=-1, wait=True)
                self.vacuum_in('ayam', 5000)
                if self.requester_callback is not None:
                    self.requester_callback(self)
                self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 2
