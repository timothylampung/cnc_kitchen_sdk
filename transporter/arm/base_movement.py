from transporter.arm.xarm_wrapper import XArmWrapperSingleton, SingletonException


class BaseMotion:
    OPEN = 200
    CLOSE = 80

    def __init__(self):
        self.requester_callback = None
        self.xArm = None
        try:
            self.xArm = XArmWrapperSingleton()
        except SingletonException as e:
            self.xArm = XArmWrapperSingleton.get_instance()

    def set_requester(self, requester_callback=None):
        self.requester_callback = requester_callback

    def start(self):
        # raise NotImplementedError()
        pass
        # if isinstance(self.xArm, XArmSDKSingleton):
        #     if self.xArm.is_connected():
        #         pass
        #     else:
        #         raise Exception('Xarm is not connected!')

    def get_eta(self):
        """in seconds"""
        raise NotImplementedError()

    def arm_can_move(self):
        if isinstance(self.xArm, XArmWrapperSingleton):
            return not self.xArm.is_arm_busy()

    def get_address(self):
        raise NotImplementedError()
