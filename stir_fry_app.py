from flask import Flask, request

from stir_fry.core.wrapper.stir_fry_sdk import StirFrySDK

app = Flask(__name__)

MODULES = []


def get_module(name):
    for module in MODULES:
        if module['name'] == name:
            return module['sdk']


@app.route('/stir/initialize/', methods=['POST'])
def initialize_modules():
    modules = request.form.get('modules')
    global MODULES
    MODULES = modules
    print(f'MODULES = {MODULES}')
    return {'message': 'stir fries initialized', 'code': 200}


@app.route('/stir/cook/', methods=['POST'])
def cook():
    json_data = request.get_json()

    module_name = json_data['module_name']
    target_temperature = json_data['target_temperature']
    durations = json_data['durations']
    need_flip = json_data['need_flip']

    sdk: StirFrySDK = get_module(module_name)
    sdk.cook(target_temperature=target_temperature, duration=durations, need_flip=need_flip)
    return {'message': 'cook completed', 'code': 200}


@app.route('/stir/pump-water/', methods=['POST'])
def pump_water():
    json_data = request.get_json()

    module_name = json_data['module_name']
    volume = json_data['target_temperature']

    sdk: StirFrySDK = get_module(module_name)
    sdk.pump_water(volume)
    return {'message': 'pump water completed', 'code': 200}


@app.route('/stir/pump-oil/', methods=['POST'])
def pump_oil():
    json_data = request.get_json()

    module_name = json_data['module_name']
    volume = json_data['target_temperature']

    sdk: StirFrySDK = get_module(module_name)
    sdk.pump_oil(volume)
    return {'message': 'pump oil completed', 'code': 200}


@app.route('/stir/set-to-temperature/', methods=['POST'])
def set_to_temperature():
    json_data = request.get_json()

    module_name = json_data['module_name']
    target_temperature = json_data['target_temperature']
    sdk: StirFrySDK = get_module(module_name)
    sdk.set_to_temperature(target_temperature)
    return {'message': 'set to temperature completed', 'code': 200}


@app.route('/stir/portion-food/', methods=['POST'])
def portion_food():
    json_data = request.get_json()

    module_name = json_data['module_name']
    sdk: StirFrySDK = get_module(module_name)
    sdk.portion_food()
    return {'message': 'Portion food completed', 'code': 200}


@app.route('/stir/pick-ingredient/', methods=['POST'])
def pick_ingredient():
    json_data = request.get_json()

    module_name = json_data['module_name']
    x = json_data['x']
    y = json_data['y']
    quantity = json_data['quantity']
    sdk: StirFrySDK = get_module(module_name)
    sdk.pick_ingredients(x, y, quantity)
    return {'message': 'Pick ingredient completed', 'code': 200}


@app.route('/stir/zero/', methods=['POST'])
def vertical_zero():
    json_data = request.get_json()

    module_name = json_data['module_name']
    sdk: StirFrySDK = get_module(module_name)
    sdk.wrapper.set_vertical_0()
    return {'message': f'Vertical {0} completed', 'code': 200}


if __name__ == '__main__':
    app.run()
