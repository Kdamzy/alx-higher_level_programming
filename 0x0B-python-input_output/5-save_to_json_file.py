#!/usr/bin/python3
"""Save object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Function the write object to a text file"""

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
