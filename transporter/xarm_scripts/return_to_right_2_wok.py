from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class ReturnToRightWokTwo(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.move_join(angle=[63.9, 97.1, -150.9, -76.6, 106.7, 126.5], radius=-1, wait=True)
            self.x_arm.move_join(angle=[52.0, 70.5, -107.5, -57.7, 76.3, 274.5], radius=-1, wait=True)
            self.x_arm.set_pause_time(1.5)
            self.x_arm.update_parameters(angle_speed=100, angle_acc=500, speed=1000, acc=500)
            self.x_arm.move_join(angle=[54.7, 46.5, -101.8, -58.6, 87.0, 120.6], radius=-1, wait=True)
            self.x_arm.move_join(angle=[91.0, -23.9, -48.7, 0.0, 72.6, 270.4], radius=-1, wait=True)
            self.x_arm.move_arc_line(-6.3, 359.6, -17.0, 180.0, 0.0, -179.4, radius=-1, wait=True)
            self.x_arm.set_gripper_position(self.OPEN, wait=True, speed=5000)
            self.x_arm.set_pause_time(1.5)

    def get_eta(self):
        return 2
