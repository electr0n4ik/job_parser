from prettytable import PrettyTable, ALL


def print_prettytable_hhru(json_data):
    table = PrettyTable()
    # table.field_names = json_data["items"][0].keys()
    table.field_names = ["id", "Вакансия", "Зарплата", "Работодатель", "Описание", "Ссылка", "Регион"]

    # Установка горизонтальных линий
    table.hrules = ALL

    for item in json_data["items"]:
        try:
            item_values = [
                item.get("id", ""),  # 1 столбец id
                item.get("name", ""),  # 2 столбец Вакансия
                f'{item.get("salary", {}).get("from", "")} '
                f'{item.get("salary", {}).get("currency", "")}',  # 3 столбец Зарплата
                item.get("employer", {}).get("name", ""),  # 4 столбец Работодатель
                f'{item.get("snippet", {}).get("requirement", "")[0:50]}...',  # 5 столбец Описание
                item.get("alternate_url", ""),  # 6 столбец Ссылка
                item.get("area", {}).get("name", "")  # 7 столбец Регион
            ]
            table.add_row(item_values)
        except:
            break

    print(table)
