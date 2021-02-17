from transporter.arm.xarm_wrapper import XArmWrapperSingleton
from transporter.xarm_scripts.base_movement import BaseMovement


class ReturnToRightWok(BaseMovement):
    def run(self):
        super().run()

        if isinstance(self.x_arm, XArmWrapperSingleton):
            joint1 = self.x_arm.arm.get_servo_angle(servo_id=1)[1]
            print(joint1)
            if joint1 > 0:
                self.x_arm.initial_position()
            else:
                pass

            self.x_arm.move_join(angle=[23.3, 18.0, -80.6, 0.0, 62.7, 23.3], radius=50, wait=False)
            if self.ingredient == 'SOLID':
                self.x_arm.move_join(angle=[33.8, 29.5, -69.2, 0.0, 39.6, 33.8], radius=50, wait=True)
            elif self.ingredient == 'LIQUID':
                self.x_arm.move_join(angle=[14.3, 26.5, -61.3, 0.1, 34.9, 14.2], radius=50, wait=True)
            else:
                self.x_arm.move_join(angle=[25.9, 19.4, -48.6, 0.0, 29.2, 25.9], radius=50, wait=True)
            self.dispense()

    def get_eta(self):
        return 2
