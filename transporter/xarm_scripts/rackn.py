from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackN(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()
            self.x_arm.set_gripper_position(self.OPEN, wait=False, speed=5000)
            self.x_arm.update_parameters(angle_speed=70, angle_acc=500, speed=1000, acc=500)
            self.x_arm.move_join(angle=[-136.0, -25.4, -42.4, -110.2, 47.7, 118.7], radius=5, wait=True)
            self.x_arm.move_arc_line(-592.4, -251.7, 316.0, 137.1, -88.6, -137.0, radius=-1, wait=True)
            self.x_arm.move_arc_line(-639.4, -251.7, 316.0, 137.1, -88.6, -137.0, radius=-1, wait=False)
            self.x_arm.set_gripper_position(self.CLOSE, wait=True, speed=5000)
            self.x_arm.update_parameters(angle_speed=14, angle_acc=100, speed=100, acc=100)
            self.x_arm.move_arc_line(-428.7, -251.7, 323.4, 137.1, -88.6, -137.0, radius=-1, wait=False)
            self.x_arm.move_join(angle=[-61.4, 0.8, -67.5, -76.9, 115.6, 116.7], radius=-1, wait=True)
            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 17