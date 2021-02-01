from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class ReturnToLeftWokTwo(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.move_join(angle=[-63.1, 109.0, -172.1, 74.2, 114.7, -122.5], radius=-1, wait=True)
            self.x_arm.move_join(angle=[-47.4, 64.3, -101.4, 56.2, 67.0, -261.8], radius=-1, wait=True)
            self.x_arm.set_pause_time(1.5)
            self.x_arm.update_parameters(angle_speed=100, angle_acc=500, speed=1000, acc=500)
            self.x_arm.move_join(angle=[-47.5, 52.3, -96.1, 60.1, 72.1, -130.5], radius=-1, wait=True)
            self.x_arm.move_join(angle=[91.0, -23.9, -48.7, 0.0, 72.6, -91.3], radius=-1, wait=True)
            self.x_arm.move_arc_line(-6.2, 359.6, -17.0, 180.0, 0.0, -177.7, radius=-1, wait=True)
            self.x_arm.set_gripper_position(self.OPEN, wait=True, speed=5000)
            self.x_arm.set_pause_time(1.5)

    def get_eta(self):
        return 2
