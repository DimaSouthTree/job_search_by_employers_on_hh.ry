from pprint import pprint

from config import config
import psycopg2
from utils import DBManager
from receiving_and_parsing import ApiGetService, GetEmployer, GetEmployerVacancies

params = config()
database_name = 'headhunter'

employers = ["Первый Бит", "Яндекс", "Whoosh", "ПАО Ростелеком",
             "Лаборатория Касперского", "ПАО Газпром автоматизация", "Т1 Интеграция",
             "IBS", "АТОЛ, группа компаний", "Sitronics Group"]
#
# data_employers = []
# data_employers_vacancies = []
# for employer in employers:
#     data_employer = GetEmployer(employer)
#     data_employers.append(data_employer.info_employer_data())
#
#     data_employer_vacancies = GetEmployerVacancies(employer)
#     data_employers_vacancies.append(data_employer_vacancies.info_vacancies_employer_data())
db = DBManager
# db.create_database('headhunter', params)
# db.save_data_employers_to_database(data_employers, 'headhunter', params)
# for data in data_employers_vacancies:
#     db.save_data_vacancies_to_database(data, 'headhunter', params)
print(db.get_companies_and_vacancies_count(database_name, params))

print(f'Чтобы получить список вакансий, Введите название компании из списка - {employers[0:]}')
print(db.get_all_vacancies('headhunter', params))

print(f'Средняя заработная плата всех вакансий: ')
print(db.get_avg_salary('headhunter', params))

print(f'Все вакассии у которых заработная плата больше средней: ')
print(db.get_vacancies_with_higher_salary('headhunter', params))

print(f'Введите ключевое слово для поиска необходимой вакансии: ')
print(db.get_vacancies_with_keyword('headhunter', params))

