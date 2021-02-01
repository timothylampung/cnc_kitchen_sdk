from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class ReturnToRightWok(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            joint1 = self.x_arm.arm.get_servo_angle(servo_id=1)[1]
            print(joint1)
            if joint1 > 0:
                self.x_arm.initial_position()
            else:
                pass
            if self.ingredient.type == Ingredient.SOLID:
                self.x_arm.move_join(angle=[-33.8, 47.3, -78.1, -1.8, 31.5, -30.8], radius=-1, wait=True)
            elif self.ingredient.type == Ingredient.LIQUID:
                self.x_arm.move_join(angle=[-16.8, 41, -63.8, -1.9, 22, -20.3], radius=-1, wait=True)
            else:
                print('wtf?')
            self.dispense()

    def get_eta(self):
        return 2
