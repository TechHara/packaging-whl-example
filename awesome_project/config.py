import json
import os


def load_config(file: str = None):
    if file is None:
        pwd = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(pwd, 'default.json')
    with open(file) as f:
        return json.load(f)