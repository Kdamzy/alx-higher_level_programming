#!/usr/bin/python3
"""From JSON string to Object"""

import json


def from_json_string(my_str):
    """Return a JSON object"""

    return json.loads(my_str)
