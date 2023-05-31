from prettytable import *
import json


def print_prettytable(json_data):
    table = PrettyTable()
    table.field_names = json_data["items"][0].keys()
    for item in json_data["items"]:
        table.add_row(item.values())

    print(table)
