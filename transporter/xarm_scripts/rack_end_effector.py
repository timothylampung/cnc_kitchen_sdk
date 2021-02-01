import time

from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackEndEffector(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.update_parameters(angle_speed=70, angle_acc=500, speed=1000, acc=500)
            self.x_arm.move_cylinder(0)
            self.x_arm.move_syringe(0)
            self.x_arm.move_puller(0)
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()
            self.x_arm.move_join(angle=[-92.9, 39.2, -104.6, -1.4, 65.9, -93.5], radius=5, wait=True)
            self.x_arm.move_cylinder(13000)
            self.x_arm.vacuum_on(0)
            # shake2
            for a in range(3):
                self.x_arm.update_parameters(speed=1000)
                self.x_arm.move_join(angle=[-94.1, 36.9, -90.6, 0.6, 50.4, -93.6], radius=5, wait=True)
                self.x_arm.move_join(angle=[-88.8, 36.9, -90.6, 0.6, 50.4, -95.1], radius=5, wait=True)
                self.x_arm.move_join(angle=[-89.1, 43.4, -103.7, 0.7, 55.5, -90.1], radius=5, wait=True)
                self.x_arm.move_join(angle=[-96.3, 44.9, -103.7, 0.7, 53.7, -94.0], radius=5, wait=True)
                self.x_arm.move_join(angle=[-94.1, 34.0, -90.6, 0.6, 50.4, -101.8], radius=5, wait=True)
                self.x_arm.move_join(angle=[-94.1, 36.9, -90.6, 0.6, 50.4, -101.8], radius=5, wait=True)

            # self.xArm.move_syringe(13000)
            # self.xArm.move_puller(9000)
            self.x_arm.move_join(angle=[-92.9, 39.2, -104.6, -1.4, 65.9, -93.5], radius=5, wait=True)
            self.x_arm.initial_position()
            self.x_arm.move_cylinder(0)
            self.x_arm.vacuum_off(0)

    def get_address(self):
        return 12
