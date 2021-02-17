#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

from flask import Flask
from flask import request
from transporter.x_arm_as_transporter import XarmTransporter
from transporter.arm.xarm_wrapper import XArmWrapperSingleton

app = Flask(__name__)


@app.route('/arm/reset/', methods=['GET'])
def reset():
    arm_wrapper: XArmWrapperSingleton = XArmWrapperSingleton.get_instance()
    arm_wrapper.reset(wait=True)
    return {'message': 'arm reset motion completed', 'code': 200}


@app.route('/arm/initial/', methods=['GET'])
def initial():
    arm_wrapper: XArmWrapperSingleton = XArmWrapperSingleton.get_instance()
    arm_wrapper.initial_position()
    return {'message': 'motion_completed', 'code': 200}


@app.route('/arm/move/', methods=['get'])
def move():
    x = request.args.get('x')
    y = request.args.get('y')
    type = request.args.get('type')
    requester = request.args.get('requester')
    quantity = request.args.get('quantity')
    print(f' x={x} y={y} type={type} quantity={quantity} requester={requester} ')

    from transporter.xarm_scripts.racka import RackA
    from transporter.xarm_scripts.rackb import RackB
    from transporter.xarm_scripts.rackc import RackC
    from transporter.xarm_scripts.rackd import RackD
    from transporter.xarm_scripts.racke import RackE
    from transporter.xarm_scripts.rackf import RackF
    from transporter.xarm_scripts.rackg import RackG
    from transporter.xarm_scripts.rackh import RackH
    from transporter.xarm_scripts.racki import RackI
    from transporter.xarm_scripts.rackj import RackJ
    from transporter.xarm_scripts.rackk import RackK
    from transporter.xarm_scripts.rackl import RackL

    x_arm_motions_directory = {
        '1': {'1': RackA(), '2': RackB(), '3': RackC(), '4': RackD(), '5': RackE(), '6': RackF()},
        '2': {'1': RackG(), '2': RackH(), '3': RackI(), '4': RackJ(), '5': RackK(), '6': RackL()},
    }

    def return_to_right_requester():
        print('return to left requester')
        from transporter.xarm_scripts.return_to_right_wok import ReturnToRightWok
        ret = ReturnToRightWok()
        ret.set_type(type)
        ret.run()

    def return_to_left_requester():
        from transporter.xarm_scripts.return_to_left_wok import ReturnToLeftWok
        ret = ReturnToLeftWok()
        ret.set_type(type)
        ret.run()

    def return_to_requester():
        if requester == 'LEFT':
            return_to_left_requester()
        else:
            return_to_right_requester()

    motion = x_arm_motions_directory[y][x]
    motion.set_requester(requester_callback=return_to_requester)
    motion.set_type(type)
    arm: XArmWrapperSingleton = XArmWrapperSingleton.get_instance()
    while arm.is_arm_busy():
        pass
    motion.run()

    return {'message': 'motion_completed'}


if __name__ == '__main__':
    XArmWrapperSingleton()
    app.run(host='192.168.1.14', port=5001)
