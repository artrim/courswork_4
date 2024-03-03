class Vacancies:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, title, url, salary_from, city):

        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.city = city

    @classmethod
    def cast_to_object_list(cls, hh_vacancies):
        """
        Преобразовывает список вакансий в список экземпляров класса
        """
        vacancies = []
        for vac_data in hh_vacancies['items']:
            title = vac_data["name"]
            url = vac_data["alternate_url"]
            if vac_data['salary']['from'] is None:
                vac_data['salary']['from'] = 0
            salary_from = vac_data["salary"]["from"]
            city = vac_data["area"]['name']
            # cls(title, url, salary_from, city)
            instance = cls(title, url, salary_from, city)
            vacancies.append(instance)
        return vacancies

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __str__(self):
        return f'Название: {self.title} \nГород: {self.city} \nЗарплата: {self.salary_from} \nURL: {self.url}\n'

    @staticmethod
    def sorted_vacancies_by_salary(vacancies):
        """
        Сортирует список вакансий по зарплате
        """
        return sorted(vacancies, reverse=True)

    @staticmethod
    def filter_vacancies_by_city(vacancies, city):
        """
        Фильтрует вакансии по городу
        """
        filter_list_by_city = []
        for vacancy in vacancies:
            if city == vacancy.city:
                filter_list_by_city.append(vacancy)
        return filter_list_by_city
