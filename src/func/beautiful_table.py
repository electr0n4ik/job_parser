from prettytable import PrettyTable, ALL


def get_prettytable():
    table = PrettyTable()
    table.field_names = ["id", "Вакансия", "Зарплата", "Работодатель", "Описание", "Ссылка", "Регион"]

    # Установка горизонтальных линий
    table.hrules = ALL
    return table


def print_prettytable_hhru(json_data, sorty: str):

    table = get_prettytable()

    for item in json_data["items"]:
        item_values = []
        item_values.append(item.get("id", ""))
        item_values.append(item.get("name", "")[:30])
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
    return table.get_string(sortby=sorty)


def print_prettytable_sj(json_data, sorty):

    table = get_prettytable()

    for item in json_data["objects"]:
        item_values = []
        item_values.append(item.get("id", ""))
        item_values.append(item.get("profession", "")[:30])
        if item.get("payment_from", "") is not None:
            item_values.append(f'{item.get("payment_from", "")} {item.get("currency", "")}')
        elif item.get("payment_to", "") is not None:
            item_values.append(f'{item.get("payment_to", "")} {item.get("currency", "")}')
        else:
            item_values.append("Не указана")
        item_values.append(item.get("firm_name", "")[:10])
        item_values.append(item.get("vacancyRichText", "")[:50])
        item_values.append(item.get("link", "")[7:])
        item_values.append(item.get("town", {}).get("title", ""))

        table.add_row(item_values)

    return table.get_string(sortby=sorty)


def print_prettytable_tv(json_data, sorty):

    table = get_prettytable()

    for item in json_data.get("results", {}).get("vacancies", []):
        item_values = []
        item_values.append(item["vacancy"].get("id", ""))
        item_values.append(item["vacancy"].get("job-name", ""))
        if item.get("salary", "") is not None:
            item_values.append(f'{item["vacancy"].get("salary", "")} руб.')
        else:
            item_values.append("Не указана")
        item_values.append(item["vacancy"].get("company", {}).get("name", ""))
        item_values.append(item["vacancy"].get("duty", ""))
        item_values.append(item["vacancy"].get("vac_url", ""))
        item_values.append(item["vacancy"].get("vacancy", {}).get("name", ""))

        table.add_row(item_values)

    return table.get_string(sortby=sorty)
