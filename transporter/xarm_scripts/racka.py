from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackA(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()
            self.x_arm.move_join(angle=[-145.9, 34.5, -91.9, 0, 57.4, 33.8], radius=-1, wait=True)
            self.vacuum_in('ayam', 5000)
            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_address(self):
        return 12
