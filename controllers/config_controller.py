import json

class ConfigController:
    def __init__(self, config_path="config/config.json"):
        self.config_path = config_path

    def update_config(self, key, value):
        """
        Update a configuration setting and save it to the JSON file.
        """
        with open(self.config_path, "r") as f:
            config = json.load(f)

        config[key] = value

        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=4)

    def get_config(self):
        """
        Retrieve the current configuration.
        """
        with open(self.config_path, "r") as f:
            return json.load(f)
