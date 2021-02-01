from ingredients.models import Ingredient
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class ReturnToLeftWok(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            joint1 = self.x_arm.arm.get_servo_angle(servo_id=1)[1]
            if joint1 > 0:
                self.x_arm.move_join(angle=[59.4, 7.5, -51.9, 0, 44.4, -31.5], radius=-1, wait=True)
            else:
                self.x_arm.initial_position()
            if self.ingredient.type == Ingredient.SOLID:
                self.x_arm.move_join(angle=[16, 34.3, -52.9, -0.8, 16.6, 19.4], radius=-1, wait=True)
            elif self.ingredient.type == Ingredient.LIQUID:
                self.x_arm.move_join(angle=[30, 46.1, -81.8, -1.9, 35.6, 31.2], radius=-1, wait=True)
            else:
                print('wtf?')
            self.dispense()

    def get_eta(self):
        return 2
