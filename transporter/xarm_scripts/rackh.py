from ingredients.models import Ingredient
from transporter.xarm_scripts.base_movement import BaseMovement
from transporter.xarm_scripts.xarm_sdk import XArmSDKSingleton


class RackH(BaseMovement):
    def run(self):
        super().run()
        if isinstance(self.x_arm, XArmSDKSingleton):
            self.x_arm.set_is_arm_busy(True)
            self.x_arm.initial_position()

            if self.ingredient.type == Ingredient.SOLID:
                self.x_arm.move_join(angle=[-152.6, -11.3, -30.3, 0, 41.6, 27.1], radius=-1, wait=True)
                self.vacuum_in('ayam', 5000)
            elif self.ingredient.type == Ingredient.LIQUID:
                self.x_arm.move_join(angle=[-136.6, 14.1, -60.9, 0.0, 46.8, 43.1], radius=-1, wait=True)
                self.suck(XArmSDKSingleton.MAX_PULLER)

            else:
                print('wtf?')
            if self.requester_callback is not None:
                self.requester_callback(self)
            self.x_arm.set_is_arm_busy(False)

    def get_eta(self):
        return 2

    def get_address(self):
        return 14
