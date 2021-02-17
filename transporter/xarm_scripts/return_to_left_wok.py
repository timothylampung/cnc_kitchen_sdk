from transporter.arm.xarm_wrapper import XArmWrapperSingleton
from transporter.xarm_scripts.base_movement import BaseMovement


class ReturnToLeftWok(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmWrapperSingleton):
            joint1 = self.x_arm.arm.get_servo_angle(servo_id=1)[1]
            if joint1 > 0:
                self.x_arm.move_join(angle=[59.4, 7.5, -51.9, 0, 44.4, -31.5], radius=-1, wait=True)
            else:
                self.x_arm.initial_position()

            self.x_arm.move_join(angle=[-20.0, 15.5, -77.2, 0.0, 61.7, -20.0], radius=50, wait=False)

            if self.ingredient == 'SOLID':
                self.x_arm.move_join(angle=[-18.7, 24.2, -54.8, 0.0, 30.7, -18.7], radius=50, wait=True)
            elif self.ingredient == 'LIQUID':
                self.x_arm.move_join(angle=[-34.0, 39.1, -84.8, 0.0, 45.8, -34.0], radius=50, wait=True)
            else:
                self.x_arm.move_join(angle=[-30.1, 22.0, -52.8, 0.0, 30.8, -30.1], radius=50, wait=True)
            self.dispense()

    def get_eta(self):
        return 2
