import requests
from get_api import GetApi


class GetApiHH(GetApi):
    """
    Класс для получения вакансий с hh api
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_api(self, keyword):
        """
        Получение вакансий с сайта hh.ru
        Возвращает json файл
        """
        response = requests.get(self.url, params={'text': keyword,
                                                  'area': 113,
                                                  'enable_snippets': 'true',
                                                  'only_with_salary': 'true',
                                                  'per_page': 100,
                                                  })
        return response.json()
