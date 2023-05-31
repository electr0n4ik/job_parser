class Vacancy:
    """
    Класс для работы с вакансиями.
    Атрибуты:
        - название вакансии;
        - зарплата;
        - работодатель;
        - краткое описание;
        - ссылка на вакансию;
        - регион.
    """
    def __init__(self, title, salary, company_name, description, link, region):
        self.title = self.validate_str(title, "title")
        self.salary = self.validate_int_float(salary, "salary")
        self.company_name = self.validate_str(company_name, "company_name")
        self.description = self.validate_str(description, "description")
        self.link = self.validate_str(link, "link")
        self.region = self.validate_str(region, "region")

    @staticmethod
    def validate_str(string_data, name_col):
        if isinstance(string_data, str):
            return string_data
        raise ValueError(f"Invalid {name_col}, {name_col} must be a string.")

    @staticmethod
    def validate_int_float(int_float, name_col):
        if isinstance(int_float, (int, float)):
            return int_float
        raise ValueError(f"Invalid {name_col}, {name_col} must be a number.")

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary