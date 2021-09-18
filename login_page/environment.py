import json

"""
Environment controls dealing with before all, before scenario, feature, steps.
Useful for loading variables such as browser path
"""

CONFIG_PATH = 'config.json'


def before_all(context):
    """
    Environment controls dealing with before all, before scenario, feature, steps
    """

    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    # Assign chrome path
        context.chrome_path = data["browser_path"]["chrome"]

