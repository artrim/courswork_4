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
