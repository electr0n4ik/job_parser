from prettytable import PrettyTable, ALL


def print_prettytable_hhru(json_data):

    table = PrettyTable()
    # table.field_names = json_data["items"][0].keys()
    table.field_names = ["id", "Вакансия", "Зарплата", "Работодатель", "Описание", "Ссылка", "Регион"]

    # Установка горизонтальных линий
    table.hrules = ALL

    for item in json_data["items"]:
        item_values = []
        item_values.append(item.get("id", ""))
        item_values.append(item.get("name", ""))
        if item.get("salary", "") is not None:
            item_values.append(f'{item.get("salary", {}).get("from", "")} '
                               f'{item.get("salary", {}).get("currency", "")}')
        elif item.get("salary", "") is not None:
            if item.get("salary", {}).get("from") is None:
                item_values.append(f'{item.get("salary", {}).get("to", "")} '
                                   f'{item.get("salary", {}).get("currency", "")}')
        else:
            item_values.append("Не указана")
        item_values.append(item.get("employer", {}).get("name", ""))
        if item.get("snippet", {}).get("responsibility", "") is not None:
            item_values.append(f'{item.get("snippet", {}).get("responsibility", "")[0:50]}...')
        else:
            item_values.append("Не указано")
        item_values.append(item.get("alternate_url", ""))
        item_values.append(item.get("area", {}).get("name", ""))

        table.add_row(item_values)

    return table
