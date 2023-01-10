#!/usr/bin/python3
"""This module contains a script that adds all arguments
    to a Python list, and then save them to a file.
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


jfile = "add_item.json"
try:
    list = load_from_json_file(jfile)
except Exception:
    list = []
finally:
    list.extend(sys.argv[1:])
    save_to_json_file(list, jfile)
