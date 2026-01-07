import json

def load_hosts(path):
    """
    Load host configuration data from a JSON file.
    """
    with open(path, "r") as file:
        return json.load(file)
