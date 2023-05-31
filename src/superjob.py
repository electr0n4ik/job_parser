from src.abc.abc_job_api import JobApi


class SuperJob(JobApi):

    def __init__(self):
        self._api_link = "https://api.superjob.ru/"

    def __str__(self):
        return "superjob.ru"

    def connect(self):
        pass

    def get_vacancies(self):
        pass
