from prettytable import PrettyTable, ALL


def print_prettytable(json_data):
    table = PrettyTable()
    # table.field_names = json_data["items"][0].keys()
    table.field_names = ["id", "name", "area"]
    # Установка горизонтальных линий
    table.hrules = ALL

    for item in json_data["items"]:
        item_values = [
            item.get('id', ''),
            item.get('name', ''),
            item.get('area', {}).get('name', '')
        ]
        table.add_row(item_values)

    print(table)
