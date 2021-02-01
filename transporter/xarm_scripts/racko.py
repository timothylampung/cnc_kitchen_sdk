from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackO(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()
            self.x_arm.set_gripper_position(self.OPEN, wait=False, speed=5000)
            self.x_arm.update_parameters(angle_speed=70, angle_acc=500, speed=1000, acc=500)
            self.x_arm.move_join(angle=[124.6, -32.0, -35.7, 104.7, 58.3, -116.7], radius=5, wait=True)
            self.x_arm.move_arc_line(-533.8, 262.0, 318.0, 84.1, -89.8, -84.1, radius=-1, wait=True)
            self.x_arm.move_arc_line(-640.0, 262.0, 318.0, 84.1, -89.8, -84.1, radius=-1, wait=False)
            self.x_arm.set_gripper_position(self.CLOSE, wait=True, speed=5000)
            self.x_arm.update_parameters(angle_speed=14, angle_acc=100, speed=100, acc=100)
            self.x_arm.move_arc_line(-406.0, 266.4, 326.0, 84.1, -89.8, -84.1, radius=-1, wait=False)
            self.x_arm.move_join(angle=[62.2, 2.4, -68.1, 78.7, 113.2, -116.6], radius=-1, wait=True)
            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 8
