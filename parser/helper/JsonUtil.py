import json

def get_unique_keys(json_object, parent_key='', unique_keys=set()):
    """
    Recursively extracts unique keys from a JSON object.

    Parameters:
    json_object (dict or list): The JSON object from which to extract keys.
    parent_key (str): The parent key string for nested keys.
    unique_keys (set): A set to store unique keys.

    Returns:
    set: A set of unique keys.Immutable
    """
    if isinstance(json_object, dict):
        for key, value in json_object.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            unique_keys.add(full_key)
            if isinstance(value, (dict, list)):
                get_unique_keys(value, full_key, unique_keys)
    elif isinstance(json_object, list):
        for item in json_object:
            get_unique_keys(item, parent_key, unique_keys)
    return unique_keys

def print_pretty_json(json_data):
    """
    Prints JSON data in a nicely formatted way.
    
    Parameters:
    json_data (dict or list): The JSON object to print.
    """
    pretty_json = json.dumps(json_data, indent=1)
    print(pretty_json)