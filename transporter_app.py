#  Copyright (c) 2021.
#  Volume Research & Development sdn. bhd.
#  Author : Timothy Lampung
#  Email : timothylampung@gmail.com
#  Contacts : 01165315133

from flask import Flask
from flask import request
from transporter.ingredient_mapping import MOTION_MAPPING
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
    quantity = request.args.get('q')
    multiplier = request.args.get('m')
    requester = request.args.get('r')
    print(f' x={x} y={y} r={requester} m={multiplier}')

    motion = MOTION_MAPPING[x][y]
    transporter = XarmTransporter(motion, requester, multiplier)
    transporter.run()
    transporter.join()
    return {'message': 'motion_completed'}


if __name__ == '__main__':
    app.run()
